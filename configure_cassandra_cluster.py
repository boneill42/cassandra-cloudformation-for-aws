#!/usr/bin/python
import json
import paramiko
from subprocess import check_output 

cassandra_seed = "" 
cluster_name = "\\'realtime-hpcc\\'" 
cassandra_yaml_location = "/etc/cassandra/conf/cassandra.yaml" 
ips = {} 

def execute_remote_command(commands, ip, key):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "Connecting to [{}]...".format(ip),
    client.connect( hostname = ip, username = "ec2-user", pkey = key )
    print "done."

    for command in commands:
        print "On [{}], executing [{}]".format(ip, command)
        (stdin, stdout, stderr) = client.exec_command(command)
#        print("\nstdout is:\n" + stdout.read() + "\nstderr is:\n" + stderr.read())
#        print "Done executing [{}] on [{}]".format(command, ip)

    client.close()

instances_json = check_output(["aws", "ec2", "describe-instances"])
instances = json.loads(instances_json)
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            if 'KeyName' in instance and instance['KeyName'] == "realtime-hpcc":
                for tag in instance['Tags']:
                    if tag['Key']=='aws:cloudformation:logical-id':
                        print "[", tag['Value'], "],   private=[", instance['PrivateIpAddress'], "], public=[", instance['PublicIpAddress'], "]"
                        cassandra_seed = cassandra_seed + "," + (str(instance['PrivateIpAddress']))
                        ips[str(instance['PublicIpAddress'])] = str(instance['PrivateIpAddress'])

key = paramiko.RSAKey.from_private_key_file("realtime-hpcc.pem")
cassandra_seed = "\\\"" + cassandra_seed[1:] + "\\\""
print "cassandra_seed = [{}]".format(cassandra_seed)
print "cluster_name = [{}]".format(cluster_name)

for public_ip in ips.keys():
    commands = []
    commands.append("sudo yum install -y cassandra21")
    commands.append("sudo python /home/ec2-user/configure_local_cassandra.py " + cassandra_yaml_location + " " + cluster_name + " " + cassandra_seed + " " + ips[public_ip])
    commands.append("sudo /etc/init.d/cassandra start")
    execute_remote_command(commands, public_ip, key)
