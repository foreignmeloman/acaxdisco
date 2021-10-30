# Ansible

## Hands-on
1. Launch a spot EC2 instance
2. Create a free account on https://freedns.afraid.org/ and register a subdomain on any available domain names and set the A record to the public IP of your EC2
3. Create an Ansible playbook to do the following automation on your EC2:
   * Install Docker
   * Create a Docker network named `application-net`
   * Create a container from `yeasy/simple-web:latest` image inside of the created network
   * Use `certbot` container or installation to get a valid TLS certificate for your subdomain (use [--test-cert](https://certbot.eff.org/docs/using.html#certbot-command-line-options) flag for testin, to avoid reaching certbot request limits)
   * Create a Nginx container inside of the created network to serve as reverse proxy for the app and redirect users to TLS encrypted URL of the website. This reverse proxy should also provide a location for certbot webroot challenge.
