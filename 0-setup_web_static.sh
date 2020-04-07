#!/usr/bin/env bash
# This bash script sets up web servers for deployment of web static.

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Start Nginx
sudo service nginx start

# Create folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Static Homepage
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to user and group
sudo chown -R ubuntu: /data/

# Config Nginx
var3="location /hbnb_static {\n alias /data/web_static/current/;\n}\n"
sudo sed -i "50i$var3" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
