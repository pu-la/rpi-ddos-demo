#!/bin/sh
mkdir ~/server
mv ./../rpi-ddos-demo ~/server
sudo apt-get install apache2 php7 libapache2-mod-php7.3
cat /etc/apache2/sites-enabled/000-default | \
sed -e 's/AllowOverride None/AllowOverride ALL/' > /etc/apache2/sites-enabled/000-default
sudo service apache2 restart
