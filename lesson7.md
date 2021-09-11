# Lesson 7: docker-compose

## Installing

https://docs.docker.com/compose/install/
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
```

## Digest docker-compose deployment example
[nginx-flask-mysql](projects/lesson7/nginx-flask-mysql)

## Hands-on
Create a docker-compose deployment with following requirements:
1. Use `alpine:3.14` image
2. Define 2 services named `log-writer` and `log-reader`
3. `log-writer` must write output of command `date` into file `/tmp/log/chronograph` (path within the container) every 3 seconds.
4. `log-reader` must start only when file `/tmp/log/chronograph` has more than 5 records.
5. `log-reader` must periodically read the last line of `/tmp/log/chronograph` and print it to its STDOUT. The result should be visible with `docker-compose logs` command.
