Install AWS CLI:
http://docs.aws.amazon.com/cli/latest/userguide/installing.html

Run:
```
aws configure
```

Set your default region to:
```
Default region name [None]: us-east-1
```


You can validate a cloudformation template with the following:
```
aws cloudformation validate-template --template-url https://s3.amazonaws.com/cloudformation-templates-us-east-1/S3_Bucket.template
```

