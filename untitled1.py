import paramiko
from paramiko import SSHClient
#import sys
import os
#import tkinter as tk

#root= tk.Tk()
#canvas1 = tk.Canvas(root, width = 300, height = 300)
#canvas1.pack()

def readip():
    try:
        ipfile1 = input("please Enter the path of your file: ")
        assert os.path.exists(ipfile1), "I did not find the file at, "+str(ipfile1)
        ipfile2 = open(ipfile1,'r+')
        print("Hooray we found your file!")
        return(ipfile2)
    except Exception as error: 
        print ("\n Error in hello program not run mybe file cannot open: \n")
        print(error)
        print("Have an Error:\n"+str(IOError))
        readip()
        

def hello ():  
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ipfile = open("ipfile.txt","r")
        ipfile = readip()
        try:
            port1 = int(input('portnumber:'))
        except ValueError:
            print ("Not a number")
        username1 = str(input('username:'))
        password1 = str(input('password:'))
        com = input('please enter your command:')
        for ip in ipfile:
            try:
                ipv4 = ip.strip()
                print("\n Connecting to: "+ipv4)
                ssh.connect(ipv4, port= port1, username= username1, password= password1)
                ssh.load_system_host_keys()
                command= open("command.txt", "r")
                #for com in command:
                try:                
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(com)
                    out = ssh_stdout
                    out = "".join(out)
                    print("Output command is:\n"+out)
                except Exception as err: 
                    print ("\n Error in for com for: \n")
                    print(err)
                    print("Command run in ip:"+ipv4+" \n Have an Error:\n"+str(IOError))
                command.close()
            except Exception as e: 
                print ("\n Error in for ipfile: \n")
                print(e)
                print("Have an Error:\n"+str(IOError))
        ipfile.close()
    except Exception as error: 
        print ("\n Error in hello program not run mybe file cannot open: \n")
        print(error)
        print("Have an Error:\n"+str(IOError))

hello()
input('please press enter to exit')
#button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
#canvas1.create_window(150, 150, window=button1)

#root.mainloop()
