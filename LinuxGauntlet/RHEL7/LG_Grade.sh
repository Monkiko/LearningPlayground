#!/bin/bash

#This script is used to grade the Support Tech Gauntlet to see if objectives
#have been met.

#Author: MonikoBytes
#Date Created: 2019-3-27
#Last Modified: 2021-7-13
#Version: 1.1.0
#OS: CentOS/RHEL 7

#Clearing screen for readability

clear

#Checking hostname of server

echo "1) Checking hostname of server"
echo -e "------------------------------\n"
echo "Server hostname: $HOSTNAME"
if [ "$HOSTNAME" == "stgauntlet" ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

#Checking for stgauntlet user, membership to wheel group, and wheel group enabled

echo "2) Checking for stgauntlet user, wheel membership, and enabled wheel group"
echo -e "--------------------------------------------------------------------------\n"
id stgauntlet &> /dev/null
USER=$?
id stgauntlet | grep wheel &> /dev/null
USERM=$?
grep ^%wheel /etc/sudoers | awk '{print$1}' &> /dev/null
WHEEL=$?

if [ "$USER" -eq 0 ]
then
  echo "stgauntlet user created"
  if [ "$USERM" -eq 0 ]
  then
    echo "stgauntlet user created AND member of wheel group"
  else
    echo "stgauntlet user created BUT not a member of wheel group"
  fi
else
  echo "stgauntlet user not found"
fi

if [ "$WHEEL" -eq 0 ]
then
  echo "wheel group is enabled"
else
  echo "wheel group is NOT enabled"
fi

if [ "$WHEEL" -a "$USERM" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

#Checking that root logins are disabled and SSH is listening on port 2432

echo "3) Logins as root are disabled and SSH is listening on prot 2432"
echo -e "----------------------------------------------------------------\n"
grep ^PermitRootLogin /etc/ssh/sshd_config | awk '{print $2}' | grep -i no &> /dev/null
RTLOGIN=$?
SSHPORT=$(grep ^Port /etc/ssh/sshd_config | awk '{print $2}')

if [ "$RTLOGIN" -eq 0 ]
then
  echo "Logins as root is disabled"
else
  echo "Logins as root is enabled"
fi

echo "SSH is listening on port $SSHPORT"

if [ "$RTLOGIN" -eq 0 ] && [ "$SSHPORT" -eq 2432 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "GRADE: FAIL"
fi
echo
echo

#Checking that ports 80, 443, 8432 were opened on iptables and checking if permanent

echo "4) Ports 80, 443, and 8432 are open on software firewall"
echo -e "--------------------------------------------------------\n"
iptables -nL | grep ":80 " | grep -i accept &> /dev/null
HTTPACT=$?
iptables -nL | grep ":443 " | grep -i accept &> /dev/null
HTTPSACT=$?
iptables -nL | grep ":2432 " | grep -i accept &> /dev/null
SSHACT=$?
firewall-cmd --zone=public --list-all --permanent | grep -w "http" &> /dev/null
HTTPPERM=$?
firewall-cmd --zone=public --list-all --permanent | grep -w "https" &> /dev/null
HTTPSPERM=$?
firewall-cmd --zone=public --list-all --permanent | grep -w "2432" &> /dev/null
SSHPERM=$?

if [ "$HTTPACT" -eq 0 ]
then
  echo "Port 80 is open"
else
  echo "Port 80 is NOT open"
fi

if [ "$HTTPSACT" -eq 0 ]
then
  echo "Port 443 is open"
else
  echo "Port 443 is NOT open"
fi

if [ "$SSHACT" -eq 0 ]
then
  echo "Port 2432 is open"
else
  echo "Port 2432 is NOT open"
fi

if [ "$HTTPPERM" -eq 0 ]
then
  echo "Port 80 is set to open on boot"
else
  echo "Port 80 is NOT set to open on boot"
fi

if [ "$HTTPSPERM" -eq 0 ]
then
  echo "Port 443 is set to open on boot"
else
  echo "Port 443 is NOT set to open on boot"
fi

if [ "$SSHPERM" -eq 0 ]
then
  echo "Port 2432 is set to open on boot"
else
  echo "Port 2432 is NOT set to open on boot"
fi

if [ "$HTTPACT" -eq 0 ] && [ "$HTTPSACT" -eq 0 ] && [ "$SSHACT" -eq 0 ] && [ "$HTTPPERM" -eq 0 ] &&
  [ "$HTTPSPERM" -eq 0 ] && [ "$SSHPERM" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo


#Checking that fail2ban is installed, running, and enabled

echo "5) Checking that fail2ban is installed, running, and enabled"
echo -e "------------------------------------------------------------\n"

rpm -qa | grep fail2ban-server &> /dev/null
F2BI=$?
systemctl status fail2ban | grep running &> /dev/null
F2BR=$?
systemctl list-unit-files | grep -i fail2ban | grep -i enabled &> /dev/null
F2BE=$?

if [ "$F2BI" -eq 0 ]
then
  echo "Installed?: Yes"
else
  echo "Installed?: No"
fi

if [ "$F2BR" -eq 0 ]
then
  echo "Running?: Yes"
else
  echo "Running?: No"
fi

if [ "$F2BE" -eq 0 ]
then
  echo "Enabled?: Yes"
else
  echo "Enabled?: No"
fi

if [ "$F2BI" -eq 0 ] && [ "$F2BR" -eq 0 ] && [ "$F2BE" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo


#Checking that Apache, MariaDB, and PHP are installed, running, and start on boot
echo "6) Checking that Apache, MariaDB, and PHP are installed, running, and start on boot"
echo -e "---------------------------------------------------------------------------------\n"

rpm -qa | grep httpd &> /dev/null
APCHI=$?
rpm -qa | grep mariadb | grep server &> /dev/null
SQLI=$?
rpm -qa | grep php &> /dev/null
PHPI=$?
systemctl status httpd | grep running &> /dev/null
APCHR=$?
systemctl status mariadb | grep running &> /dev/null
SQLR=$?
systemctl list-unit-files | grep -i httpd | grep -i enabled &> /dev/null
APCHE=$?
systemctl list-unit-files | grep -i mariadb | grep -i enabled &> /dev/null
SQLE=$?

if [ "$APCHI" -eq 0 ]
then
  echo "Apache Installed?: Yes"
else
  echo "Apache Installed?: No"
fi

if [ "$SQLI" -eq 0 ]
then
  echo "MariaDB Installed?: Yes"
else
  echo "MariaDB Installed?: No"
fi

if [ "$PHPI" -eq 0 ]
then
  echo "PHP Installed?: Yes"
else
  echo "PHP Installed?: No"
fi

if [ "$APCHR" -eq 0 ]
then
  echo "Apache Running?: Yes"
else
  echo "Apache Running?: No"
fi

if [ "$SQLR" -eq 0 ]
then
  echo "MariaDB Running?: Yes"
else
  echo "MariaDB Running?: No"
fi

if [ "$APCHE" -eq 0 ]
then
  echo "Apache Enabled?: Yes"
else
  echo "Apache Enabled?: No"
fi

if [ "$SQLE" -eq 0 ]
then
  echo "MariaDB Enabled?: Yes"
else
  echo "MariaDB Enabled?: No"
fi

if [ "$APCHI" -eq 0 ] && [ "$SQLI" -eq 0 ] && [ "$PHPI" -eq 0 ] && [ "$APCHR" -eq 0 ] && [ "$SQLR" -eq 0 ] && [ "$APCHE" -eq 0 ] && [ "$SQLE" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

#Checking that vhost was created and index.html was created with correct content

echo "7) Checking that stgauntlet.tech vhost file was created and index.html was created"
echo -e "----------------------------------------------------------------------------------\n"

INDEX=$(cat /var/www/vhosts/stgauntlet.tech/index.html | grep -w "I made Apache work!")

if [ -e /etc/httpd/vhost.d/stgauntlet.tech.conf ]
then
  echo "Vhost created?: Yes"
else
  echo "Vhost created?: No"
fi

if [ -e /var/www/vhosts/stgauntlet.tech/index.html ]
then
  echo "index.html created?: Yes"
  if [ "$INDEX" == "I made Apache work!" ]
  then
    echo "Correct content?: Yes"
  else
    echo "Correct content?: No"
  fi
else
  echo "index.html created?: No"
fi

if [ -e /etc/httpd/vhost.d/stgauntlet.tech.conf ] && [ -e /var/www/vhosts/stgauntlet.tech/index.html ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

#Checking that wordpress was installed in wordpress directory

echo "8) Checking that wordpress was installed in wordpress directory and Apache is serving Wordpress"
echo -e "-----------------------------------------------------------------------------------------------\n"
curl -sk https://localhost/wordpress/ | grep 'Powered by WordPress' &> /dev/null
WP=$?

if [ -d /var/www/vhosts/stgauntlet.tech/wordpress ]
then
  echo "Wordpress directory created?: Yes"
  if [ -e /var/www/vhosts/stgauntlet.tech/wordpress/wp-config.php ]
  then
    echo "Wordpress installed?: Yes"
  else
    echo "Wordpress installed?: No"
  fi
else
  echo "Wordpress directory created?: No"
fi

if [ "$WP" -eq 0 ]
then
  echo "Apache serving Wordpress?: Yes"
else
  echo "Apache serving Wordpress?: No"
fi

if [ -d /var/www/vhosts/stgauntlet.tech/wordpress ] && [ -e /var/www/vhosts/stgauntlet.tech/wordpress/wp-config.php ] && [ "$WP" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

#Checking that the MariaDB version is 10.0.*

echo "9) Checking that MariaDB is running on version 10.0"
echo -e "---------------------------------------------------\n"
MRV=$(MariaDB -e "select if(VERSION() >= '10.0.%' ,1,0)\G" | awk -F: '{print $2}' | grep -v -e '^[[:space:]]*$')

if [ "$MRV" -eq 1 ]
then
  echo "MariaDB is running on version 10.0?: Yes"
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "MariaDB is running on version 10.0?: No"
  echo "Grade: FAIL"
fi
echo
echo

#Checking that MariaDB replication is configured

echo "10) Checking that MySQL Replication has been configured"
echo -e "-------------------------------------------------------\n"
SIR=$(mysql -e 'show slave status\G' | grep -i 'slave_io_running:' | awk '{print $2}')
SSR=$(mysql -e 'show slave status\G' | grep -i 'slave_sql_running:' | awk '{print $2}')

if [ "$SIR" == "Yes" ] && [ "$SSR" == "Yes" ]
then
  echo "MySQL Replication configured?: Yes"
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "MySQL Replication configured?: No"
  echo "Grade: FAIL"
fi
echo
echo

#SSL Cert creation and installation

echo "11) Checking that SSL certificate was created and installed"
echo -e "-----------------------------------------------------------\n"
find / -type f -name stgauntlet.tech.key &> /dev/null
KEY=$?
find / -type f -name stgauntlet.tech.crt &> /dev/null
CERT=$?

if [ "$KEY" -eq 0 ]
then
  echo "Private key created?: Yes"
  if [ "$CERT" -eq 0 ]
  then
    echo "SSL certificate created?: Yes"
    echo "Grade: PASS"
    echo "PASS" >> ./stg_score.txt
  else
    echo "SSL certificate created?: No"
  fi
else
  echo "Private key created?: No"
fi

if [ "$KEY" -ne 0 ] || [ "$CERT" -ne 0 ]
then
  echo "Grade: FAIL"
fi
echo
echo


# Apache HTTP redirect checker

echo "12) Checking that HTTP traffic was redirected to HTTPS"
echo -e "------------------------------------------------------\n"
curl -Is localhost | grep -E " 302 |Location: https:" &> /dev/null
REDRT=$?

if [ "$REDRT" -eq 0 ]
then
  echo "HTTP requests redirected to HTTPS?: Yes"
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "HTTP requests redirected to HTTPS?: No"
fi

if [ "$REDRT" -ne 0 ]
then
  echo "Grade: FAIL"
fi
echo
echo

#Nginx installation, listening on port 8080, root is /var/www/vhosts/staging.stgauntlet.tech, index.html, and open firewall

echo "13) Checking that Nginx is installed, listening on port 8080, document root is configured, index.html is configured, firewall port is open"
echo -e "------------------------------------------------------------------------------------------------------------------------------------------\n"
rpm -qa | grep nginx &> /dev/null
NGXI=$?
systemctl status nginx | grep running &> /dev/null
NGXR=$?
systemctl list-unit-files | grep -i nginx | grep -i enabled &> /dev/null
NGXE=$?
netstat -plnt | grep ":8080 " | grep -i nginx &> /dev/null
NGXACT=$?
NGXRT=$(grep root /etc/nginx/conf.d/staging.stgauntlet.tech.conf | awk '{print $2}' | awk -F\; '{print $1}')
NGXINDEX=$(cat /var/www/vhosts/staging.stgauntlet.tech/index.html | grep -w "I made Nginx work!")
firewall-cmd --zone=public --list-all --permanent | grep -w "8080" &> /dev/null
NGXPERM=$?

if [ "$NGXI" -eq 0 ]
then
  echo "Nginx installed?: Yes"
else
  echo "Nginx installed?: No"
fi

if [ "$NGXR" -eq 0 ]
then
  echo "Nginx running?: Yes"
else
  echo "Nginx running?: No"
fi

if [ "$NGXE" -eq 0 ]
then
  echo "Nginx enabled?: Yes"
else
  echo "Nginx enabled?: No"
fi

if [ "$NGXACT" -eq 0 ]
then
  echo "Is Nginx listening on port 8080: Yes"
else
  echo "Is Nginx listening on port 8080: No"
fi

if [ "$NGXRT" == "/var/www/vhosts/staging.stgauntlet.tech" ]
then
  echo "DocumentRoot configured correctly?: Yes"
else
  echo "DocumentRoot configured correctly?: No"
fi

if [ "$NGXINDEX" == "I made Nginx work!" ]
then
  echo "Nginx index.html created?: Yes"
else
  echo "Nginx index.html created?: No"
fi

if [ "$NGXPERM" -eq 0 ]
then
  echo "Firewall has port 8080 open?: Yes"
else
  echo "Firewall has port 8080 open?: No"
fi

if [ "$NGXI" -eq 0 ] && [ "$NGXR" -eq 0 ] && [ "$NGXE" -eq 0 ] && [ "$NGXACT" -eq 0 ] &&
  [ "$NGXRT" == "/var/www/vhosts/staging.stgauntlet.tech" ] && [ "$NGXINDEX" == "I made Nginx work!" ] &&
  [ "$NGXPERM" -eq 0 ]
then
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Grade: FAIL"
fi
echo
echo

# Checking if upload max filesize has been updated in /etc/php.ini

echo "14) Checking that upload max filesize has been updated"
echo -e "------------------------------------------------------\n"
PHPINI=$(grep "upload_max_filesize" /etc/php.ini | grep -v "^#upload_max_filesize" | awk '{print $3}')

if [ "$PHPINI" == "40M" ]
then
  echo "Was upload_max_filesize updated correctly?: Yes"
  echo "Grade: PASS"
  echo "PASS" >> ./stg_score.txt
else
  echo "Was upload_max_filesize updated correctly?: No"
  echo "Grade: FAIL"
fi
echo
echo

#Provide Score

Correct=$(grep PASS ./stg_score.txt | wc -l)
Score=$(( Correct * 100 ))
Total=$(( Score / 15 ))
echo "Score: $Total/100"
echo '' > ./stg_score.txt
