!#/bin/bash

PACHE
yum install -y httpd httpd-devel httpd-tools
chkconfig --add httpd
chkconfig httpd on
service httpd stop

rm -rf /var/www/html
ln -s /vagrant /var/www/html

service httpd start

#PHP
yum install -y php php-cli php-common php-devel php-mysql



# Download stater content
cd /vagrant
sudo -u vagrant wget -q https://raw.githubusercontent.com/KrauserSan/MOOC-Learning/master/Vagrant/files/index.html
sudo -u vagrant wget -q https://raw.githubusercontent.com/KrauserSan/MOOC-Learning/master/Vagrant/files/info.php



service httpd restart
