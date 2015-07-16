This repo contains scripts for installing Cassandra on a AWS cluster.

It works in conjunction with the CloudFormation template found here:
https://github.com/boneill42/hpcc-cassandra-cluster-on-aws


You can kick off the cloud formation with:
```
create_stack.sh
```

Then, you can check on the status of the cloud with:
```
get_status.sh
```

After the cloud forms, you simply run:
```
python configure_cassandra_cluster.py
```

This will install and configure Cassandra on each of the nodes.

Once you are done, you can run:
```
delete_stack.sh
```

This will tear down the EC2 instances.


