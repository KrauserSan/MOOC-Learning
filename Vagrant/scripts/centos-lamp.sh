#!/bin/bash

#GENERAL PACKAGES
yum update -y --exclude=kernel
yum install -y nano git unzip screen

#APACHE
yum install -y httpd httpd-devel httpd-tools
chkconfig --add httpd
chkconfig httpd on
service httpd stop

rm -rf /var/www/html
ln -s /vagrant /var/www/html

service httpd start

#PHP
yum install -y php php-cli php-common php-devel php-mysql

#MYSQL
yum install -y mysql mysql-server mysql-devel
chkconfig --add mysqld
chkconfig mysqld on
service mysqld start

mysql -u root -e "SHOW DATABASES";

# Download stater content
cd /vagrant
sudo -u vagrant wget -q https://raw.githubusercontent.com/KrauserSan/MOOC-Learning/master/Vagrant/files/index.html
sudo -u vagrant wget -q https://raw.githubusercontent.com/KrauserSan/MOOC-Learning/master/Vagrant/files/info.php



service httpd restart

