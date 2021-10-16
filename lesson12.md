# ECS

## Hands-on
Overview: Create a Gitlab CI/CD pipeline to build and deploy a web app to ECS.

Region `eu-west-1 (Ireland)`

1. Create a new GitLab project en populate it with files from this repo: https://gitlab.com/iamads/my-ecs-demo/

2. Create and configure an EC2 GitLab runner capable of building Docker images. Disable shared runners for your project.
> Previous hands-on tutorial:  
> https://www.digitalocean.com/community/tutorials/how-to-set-up-a-continuous-deployment-pipeline-with-gitlab-ci-cd-on-ubuntu-18-04  
> GitLab runner with dind:  
> https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#docker-in-docker-with-tls-enabled  

3. Create an ECS Cluster named `name-surname-cluster`, template `Networking only`.
4. Create a Task Definition named `name-surname-task-def`.
> Task execution Role: `ecsTaskExecutionRole`
> Container name: `web`, image `<your_gitlab_image_registry>`
5. Create a Service named `name-surname-svc`.
6. Follow the official GitLab docs to deploy the container to ECS:
> https://docs.gitlab.com/ee/ci/cloud_deployment/index.html#deploy-your-application-to-the-aws-elastic-container-service-ecs
<!-- > Runner Role: `ec2-ecr-access` -->
<!-- > ECR Docker login example:   -->
<!-- > https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html#examples   -->




