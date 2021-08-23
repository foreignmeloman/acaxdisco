# Lesson 4: Web app service under a reverse proxy

## Hands-on
1. Download `app.txz` from provided link, extract the contents and follow `README.md` instructions to run local server.
2. Setup a systemd service for the app.
3. Install nginx and python3 if needed.
4. Configure reverse proxy to make the app available on port 80.
5. Write a parser script to analyze nginx access log and output top 5 accessed locations with quanifiers.
Sample output:
```
     37 /
     20 /static/images/wa.png
     20 /static/images/dexter.gif
     20 /static/css/custom.css
      2 /static/images/tasker.png
```
