# Support Tech Gauntlet - Linux

The following will be a list of tasks/challenges that are designed to give you an idea of some of the technologies/programs that are supported by the Linux SysAds. The idea here is to practice working with Linux Cloud Servers as well as become more familiar with our Cloud control panel.

##### Advice:
* Work on your google-fu. We come across all kinds of programs and applications that we aren't always familiar with and have look up information frequently. Use this as an opportunity to strengthen this skill without a customer on the phone demanding results right now.

* If you break something, GOOD! Learn from it and if possible troubleshoot it, work through it, and you will be stronger for it.

* PRACTICE PRACTICE PRACTICE! The only way you will be more comfortable working on the command line is to consistently work on the command line. Reading is good but only takes you so far...

* If you are unable to perform a task due version/distro differences, can you explain why it is not possible?


##### Tasks:

1) Spin up a CentOS 6 cloud server. Leave the default name while building the server. After it has been built, rename the server in the control panel to STGauntlet and adjust the hostname within the OS to "stgauntlet". Make sure the change is permanent.

2) Create the stgauntlet user account, add them to the wheel group, make sure the wheel group is enabled in /etc/sudoers.

3) Configure the ssh service to not allow root logins. Change the port this service is listening on to 2432. Restart this service after making these changes.

4) Open ports 443, 80 and port 2432 (the new SSH port) on the firewall. Make sure these rules are permanent.

5) Install the fail2ban package and start the service. Makes sure the service is set to start on boot.

6) Install the LAMP stack. Start the services and have them start on boot.

7)  Create a vhost in /etc/httpd/vhost.d/ for the stgauntlet.tech domain. Create a index.html file in your document root (/var/www/vhosts/stgauntlet.tech/) that displays "I made Apache work!".

8) Install Wordpress in a /wordpress directory located in your document root.

9) Update MySQL to 5.6 (MariaDB 10.0 in the case of CentOS 7).

10) Take an image and build a new server. Setup MySQL replication between the two servers making the original server the slave (Don't forget to delete your image when you are done with this exercise).

11) Update PHP from the default version to PHP 5.6 (Use yum replace).

12) Install the monitoring agent and driveclient. Once this is configured, create a file called backup_test in /root and then take a backup of the /root directory. Once completed, delete backup_test and then restore this file from the back up to /home/stgauntlet/

13) Create a Self-Signed SSL Certificate (name the files stgauntlet.tech.crt and stgauntlet.tech.key), install it, and configure stgauntlet.tech to redirect all HTTP traffic to HTTPS.

14) Install Nginx, configure it to listen on port 8080, configure a new subdomain (staging.stgauntlet.tech), make your document root /var/www/vhosts/staging.stgauntlet.tech/, and create an index.html file with "I made Nginx work!" in it. Open port 8080 on your firewall.

15) Edit php.ini to increase the upload max filesize to 40M

16) Do all the above using CentOS 7 (Use MariaDB instead of MySQL). Repeat for Ubuntu 14.04. Repeat again for Ubuntu 16.04.

Extra Credit: In MySQL, create a database called "Playground". Add a table called movies with the following columns: "id | name | genre | year ". The id column should auto-increment. Add entries with movies you own. For example:

```
Select * from movies;
+----+------------------------------------+----------------+------+
| id | name                               | genre          | year |
+----+------------------------------------+----------------+------+
|  1 | Star Wars IV: A New Hope           | Sci-Fi/Fantasy | 1977 |
|  2 | Star Wars V: Empire Strikes Back   | Sci-Fi/Fantasy | 1980 |
|  3 | Star Wars VI: Return of the Jedi   | Sci-Fi/Fantasy | 1983 |
|  4 | Star Wars I: The Phantom Menace    | Sci-Fi/Fantasy | 1999 |
|  5 | Star Wars II: Attack of the Clones | Sci-Fi/Fantasy | 2002 |
|  6 | Star Wars III: Revenge of the Sith | Sci-Fi/Fantasy | 2005 |
|  7 | Star Wars VII: The Force Awakens   | Sci-Fi/Fantasy | 2015 |
+----+------------------------------------+----------------+------+
```

Extra Practice:

Work on your Regex -> https://alf.nu/RegexGolf

Need shorter tasks? Click [here](https://one.rackspace.com/display/~ian8775/Quick+Linux+Tasks "Quick Linux Tasks")
