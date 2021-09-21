# AWS: S3 and EC2

## S3

Login to your AWS console, search for S3 and create a bucket.

If you don't have a user with Access key ID and Secret access key, then create one.

First install the CLI tools: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

To enable bash completion add this to your `.bashrc`:
```
complete -C '/usr/local/bin/aws_completer' aws
```

Now login to AWS console end from 'IAM configure the CLI credentials:
```
$ aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: 
Default output format [None]:
```

You can use `aws --profile some_name_here` argument to store the configuration in a separate profile. Useful when you have multiple profiles.

We can use aws cli for all sorts of actions, including uploading a file into our s3 bucket. Let's do it.
```
$ aws s3 ls s3://your_bucket_name_here
$ echo "some text" > payload.txt
$ aws s3 cp payload.txt s3://your_bucket_name_here
upload: ./payload.txt to s3://your_bucket_name_here/payload.txt
$ aws s3 ls s3://your_bucket_name_here
```

Now lets host a static site inside of a static bucket
https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html#step2-create-bucket-config-as-website
