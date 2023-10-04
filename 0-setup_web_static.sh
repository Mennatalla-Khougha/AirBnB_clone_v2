#!/usr/bin/env bash
#sets up the web servers for the deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared 
mkdir -p /data/web_static/releases/test/

echo "Hello world" >  /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current 

chown -R ubuntu:ubuntu /data/

sed -i "/server_name _;/a \
\
    location /hbnb_static/ { \
        alias /data/web_static/current/;\
        index index.html;\
    }" /etc/nginx/sites-available/default

service nginx restart
