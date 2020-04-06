#!/usr/bin/env bash
# This bash script sets up web servers for deployment of web static.
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/current /data/web_static/releases/test/

sudo chown -R ubuntu: /data/

var="location /hbnb_static/ {\n root /data/web_static/current/;\n}\n"
sudo sed -i "50i$var" /etc/nginx/sites-available/default

sudo service nginx restart
