Writeup 3 - OSINT II, OpSec and RE
======

Name: *Francis-Jide Adeosun*
Section: *Francis-Jide Adeosun*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Francis-Jide Adeosun*

## Assignment 3 Writeup

### Part 1 (100 pts)
*1) One vulnerability of the Fred Krueger was his use of familiar username and password. His username was easy to figure out by trying a couple of variations of the username Kruegster1990. His instagram account gave away his love of Pokemon and gave us a possible option as to what the password is. After using the wordlist to bruteforce his password we find that pokemon is truly his password. I would suggest a multi-factor authentication system for the servers password. Another option is the use of SSH Key authenticationSetting up SSH key authentication allows you to disable password-based authentication. According to DigitalOcean SSH keys more bits of data than a password thus increasing the difficulty and number of passwords to run through.
2) Another vulnerability is the version of their server operating system. Their system is Apache/2.4.18(Ubuntu) and the latest is 2.4.34 Just looking through cvedetails.com one can find a number of vulnerabilities to their OS version. I would suggest keeping your OS updated as updates fix security issues and a number of other things. 
Exhibit A: "In Apache httpd 2.2.x before 2.2.33 and 2.4.x before 2.4.26, use of the ap_get_basic_auth_pw() by third-party modules outside of the authentication phase may lead to authentication requirements being bypassed." 
Exhibit B: "In Apache httpd before 2.2.34 and 2.4.x before 2.4.27, the value placeholder in [Proxy-]Authorization headers of type 'Digest' was not initialized or reset before or between successive key=value assignments by mod_auth_digest. Providing an initial key with no '=' assignment could reflect the stale value of uninitialized pool memory used by the prior request, leading to leakage of potentially confidential information, and a segfault in other cases resulting in denial of service."
3)Having the private port 1337 open and not protected enabled us to brute force the username and password. Giving us access to private and vulnerable areas of the system. The use of a firewall will restrict access to ports and service you dont want the public to access. It reduces the amount of components vulnerable to attack. 
 *
