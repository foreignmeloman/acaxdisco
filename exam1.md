
1. Create systemd service `exporter.service` to run prometheus node_exporter (https://prometheus.io/docs/guides/node-exporter) on loopback IP of the host on 9100 port.
2. Setup prometheus server (https://prometheus.io/docs/prometheus/latest/installation/#installation), with a docker container running in the `host` network using the following configuration below.

prometheus.yaml (Decode it!):
```
Z2xvYmFsOgogIHNjcmFwZV9pbnRlcnZhbDogMTVzCnNjcmFwZV9jb25maWdzOgotIGpvYl9uYW1l
OiAnISEhUkVQTEFDRV9IRVJFX1lPVVJfTkFNRV9ET1RfU1VSRU5BTUVfSU5fTE9XRVJDQVNFISEh
IScKICBzdGF0aWNfY29uZmlnczoKICAtIHRhcmdldHM6IFsnMTI3LjAuMC4xOjkxMDAnXQo=
```
3. Write a script called `prom_setup.sh` which will automate task 1 and 2, including downloading the archive form the web.
4. Get the Python app code from remote repository: https://gitlab.com/foreignmeloman/flaskex .
5. Create a new public repository `flaskex` with the Python app code and push it.
6. Build docker image for the Python app and push it to your GitLab image registry for `flaskex` repository.
7. Using nginx reverse proxy make the app available on port 80.
8. Add a directory named `exam` to `flaskex` repository and add `exporter.service` from task 1, `prom_setup.sh` from task 3 and `Dockerfile` from task 6 to it and push it.
