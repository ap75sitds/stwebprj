#!/bin/bash
nginx -v
sudo ln -s /home/alex/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
