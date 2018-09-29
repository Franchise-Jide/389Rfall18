Writeup 3 - Pentesting I
======

Name: *Francis-Jide Adeosun*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Francis-Jide Adeosun*

## Assignment 4 Writeup

### Part 1 (45 pts)
*CMSC389R-{p1ng_as_a_$erv1c3} 
"142.93.117.193   shell;   cd /home; ls; cat flag.txt"
First, I created the socket then connected it to the host and the port. The prompt was displayed and asked for and IP address. I put in the admin address, but it didn’t do anything it was just blank for a while. I fiddle with this for a long time then I realized that I need “\n” at the end of what I send to the server.  I then proceeded to input the servers IP address and I just got a load of information taking about pings and the number of packets sent and received. I then tried to execute the command with one of the commands listed in part two, but it didn’t work. I then proceeded to search up what command injection was. After I found it I realized that I needed to put in the IP address and add a couple spaces and place the desired command at the end. I first tried “shell” but nothing showed up then I tried “ls” then nothing showed again. So then I combined the two and injected the command “shell;ls”. The directories and everything of the server was shown and I was elated. After that I started nesting commands to look for the flag. The first place I checked was the home directory because in the class pdf the flag was there, so I thought “why not?”. I checked inside and found the “flag.txt” file and then nested the “cat flag.txt” command to the end of the commands I had previously used. 
I found the uptime script in the opt/container_startup.sh
I guess he could hide the script my adding a "." before the file name or he could not take the input directly and limit the amount of character to highest number of characters of the IP addresses he wishes to check. *

### Part 2 (55 pts)
*First thing I did was to create while loop so that I could continuously input the commands. Inside the loop I placed the execute_cmd inside the loop. I used raw_input to print the shell prompt and place the user’s entered data into variable called cmd. I noticed that the data received from the server kept printing and as well as the data I receive after I sent my information printed 3 times. I realized that I had to remove the print statements In the execute_cmd and instead return the data received. The next thing I moved unto was to display the prompt which took the most time. I used the execute_cmd to send the “pwd” command to retrieve the current directory each time. I ran the program, and nothing wouldn’t show up because of the newline at the end. After removing the newline everything seemed to work until I typed the “ls” command. The directory name changed to the output of the “ls” command, so I realized that I had to wrap the change directory piece of code in an if statement to only run is the command contains the string “cd”. I searched the internet how to split strings as well has to strip the newline. I stored the “shell” command as well as the change directory command in the variable ‘loaded’. I thought I was finished until I tried the pull command. I couldn’t figure out what to do so I quit and waited till the next day so ask the TA’s. The TA showed me that the four different options should occur at the > stage before we actually enter the server. So, to fix that I put the original code I had in a while loop set to exit on “quit” and within that while loop added if statements for the “pull” and “help”. The help command code was a breeze. For “pull” I had to search how to do file operations. After writing the open, write and close command I ran the program and It didn’t work. I realized that the mode for open() has to be a char not string. After fixing that everything worked! YAY!*