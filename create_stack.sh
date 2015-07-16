aws cloudformation create-stack --capabilities CAPABILITY_IAM --stack-name realtime-hpcc --template-body https://s3.amazonaws.com/realtime-hpcc/MyHPCCCloudFormationTemplate.json --parameters \
   ParameterKey=HPCCPlacementGroup,ParameterValue=realtime-hpcc \
   ParameterKey=HPCCPlatform,ParameterValue=HPCC-Platform-5.2.2-1 \
   ParameterKey=KeyPair,ParameterValue=realtime-hpcc \
   ParameterKey=MasterInstanceType,ParameterValue=c3.2xlarge \
   ParameterKey=NumberOfRoxieNodes,ParameterValue=1 \
   ParameterKey=NumberOfSlaveInstances,ParameterValue=1 \
   ParameterKey=NumberOfSlavesPerNode,ParameterValue=2 \
   ParameterKey=RoxieInstanceType,ParameterValue=c3.2xlarge \
   ParameterKey=ScriptsS3BucketFolder,ParameterValue=s3://realtime-hpcc/ \
   ParameterKey=SlaveInstanceType,ParameterValue=c3.2xlarge \
   ParameterKey=UserNameAndPassword,ParameterValue=realtime/foobar99
