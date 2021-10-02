## Hands-on
Create your own VPC with with private and public subnets

Steps:
1. Create a new VPC with a name `name-surname-vpc`
> * Use `10.X.0.0/16` CIDR where X = your_BD_month + your_BD_day + your_age (we do this to get a unique X value)
2. Create 2 subnets:
> * `10.X.1.0/24` - name: `name-surname-private`, AZ: eu-west-1a, auto-assign IP: disabled
> * `10.X.2.0/24` - name: `name-surname-public`, AZ: eu-west-1b
3. Create an Internet Gateway named `name-surname-igw`, attach it to your VPC
4. Create a NAT Gateway named `name-surname-nat` inside of your public subnet
> * Find and give name `name-surname-eip` to your Elastic IP allocation
5. Apply the following configuration to the main route table of your VPC:
> * name: `name-surname-private`
> * add route `0.0.0.0/0` and target it to your NAT Gateway
> * associate your private subnet with this route table
6. Create a new route table in your VPC:
> * name: `name-surname-public`
> * add route `0.0.0.0/0` and target it to your Internet Gateway
> * associate your public subnet with this route table
7. Create a private EC2 instance:
> * name: `name-surname-ec2-private`
> * vpc: your VPC
> * subnet: your private subnet
> * security group: create new one named `name-surname-sg-private` and allow port 22 from your public subnet CIDR
8. Create a public EC2 instance:
> * name: `name-surname-ec2-public`
> * vpc: your VPC
> * subnet: your public subnet
> * security group: create new one named `name-surname-sg-public` and allow port 22 from your current IP
9. Find a way to SSH to your private EC2 instance and see if you have internet connectivity
10.  Remove `0.0.0.0/0` route from your private route table and see if you still have internet connectivity
