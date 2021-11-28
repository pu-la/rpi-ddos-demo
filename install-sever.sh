#!/bin/sh
sudo mkdir ~/server
sudo mv ./../rpi-ddos-demo ~/server
sudo apt-get install apache2
sudo service apache2 restart
