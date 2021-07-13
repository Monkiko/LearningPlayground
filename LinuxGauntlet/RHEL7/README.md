# Support Tech Gauntlet - Linux

The following will be a list of tasks/challenges that are designed to give you an idea of some of the technologies/programs that are supported by Linux SysAds working with CentOS 7.

##### Advice:
* Work on your google-fu. We come across all kinds of programs and applications that we aren't always familiar with and have to look up information frequently. Use this as an opportunity to strengthen this skill without a production emergency.

* If you break something, GOOD! Learn from it and if possible troubleshoot it, work through it, and you will be stronger for it.

* PRACTICE PRACTICE PRACTICE! The only way you will be more comfortable working on the command line is to consistently work on the command line. Reading is good but only takes you so far...


##### Tasks:

1)  Log in to server1 and change the hostname within the OS to "stgauntlet". Make sure the change is permanent.

2)  Create the stgauntlet user account, add them to the wheel group, make sure the wheel group is enabled in /etc/sudoers.

3)  Configure the ssh service to not allow root logins. Change the port this service is listening on to 2432. Restart this service after making these changes.

4)  Open ports 443, 80 and port 2432 (the new SSH port) on the firewall. Make sure these rules are permanent.

5)  Install the fail2ban package and start the service. Makes sure the service is set to start on boot.

6)  Install the LAMP stack. Start the services and have them start on boot.

7)  Create a vhost in /etc/httpd/vhost.d/ for the stgauntlet.tech domain. Create a index.html file in your document root (/var/www/vhosts/stgauntlet.tech/) that displays "I made Apache work!".

8)  Install Wordpress in a /wordpress directory located in your document root.

9)  Update MariaDB to 10.0.

10) Setup MySQL replication between the two servers making server1 the replicant (setup /root/.my.cnf to allow noninteractive login to MySQL root user).

11) Create a Self-Signed SSL Certificate (name the files stgauntlet.tech.crt and stgauntlet.tech.key) and install it.

12) Configure stgauntlet.tech to redirect all HTTP traffic to HTTPS.

13) Install Nginx, configure it to listen on port 8080, configure a new subdomain (staging.stgauntlet.tech), make your document root /var/www/vhosts/staging.stgauntlet.tech/, and create an index.html file with "I made Nginx work!" in it. Open port 8080 on your firewall.

14) Edit php.ini to increase the upload max filesize to 40M

Extra Credit: In MariaDB, create a database called "Playground". Add a table called movies with the following columns: "id | name | genre | year ". The id column should auto-increment. Add entries with movies you own. For example:

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