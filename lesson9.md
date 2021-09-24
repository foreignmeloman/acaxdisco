# EC2 and RDS

## Hands-on
Deploy a Wordpress site using EC2 and RDS.

Requirements:
* Use official `wordpress:latest` image from Docker hub.
* Use the following naming scheme for the instances:
> * EC2: `name.surname-ec2`
> * RDS: `name-surname-rds`
* Use `Amazon Linux` or `Ubuntu` AMI and `t2.micro` instance type for EC2
* Use `name.surname` format when creating key pair for your EC2
* Use `MySQL` engine type and `Free tier` template for RDS
* Create your own security groups for EC2 and RDS named `name.surname-sg-ec2` and `name.surname-sg-rds` respectively
* Site should be available only form the current public IP of our class WiFi
* None of the services should be publicly available
* The landing page should say `Hello from Name Surname!` instead of `Hello World!`
