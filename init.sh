#!/bin/bash
nginx -v
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo unlink /etc/nginx/sites-enabled/default
sudo service nginx start
sudo service nginx status