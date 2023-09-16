import socket as s
import os
import sys
import re
import time

def enter_Host():
    HOST = input("Write your Host Name: \nYou can check your Host address by the below following steps\n1. Open CMD\n2. Type ipconfig\n3. Check for the Ethernet/Wifi IPv4 address\n")
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(pattern, HOST) is not None:
        print(f"Your IP/Host Address is {HOST} ")
        time.sleep(2)
        return HOST
    else:
        print("Re-Run the program you have entered the wrong IP address.\nPlease follow the above steps nicely")
        time.sleep(2)
        sys.exit()

def choose_Port():
    PORT = int(input("Choose a port number to try to keep it in the range of 3000 to 65535: "))
    if PORT in range(3000,65536):
        pass
    else:
        print("Check for a proper port number!...")
        time.sleep(2)
        sys.exit()
    print(f"Your port number is: {PORT}")
    time.sleep(2)
    return PORT

def binding(HOST, PORT):
    peer1 = s.socket(s.AF_INET, s.SOCK_STREAM)
    peer1.bind((HOST, PORT))
    peer1.listen(1)

    while True:
        comm, add = peer1.accept()
        print(f"You are connected to the Peer 2 with IP {add}\n")
        time.sleep(2)

        print(f"Message received form the Peer 2 is:\n{comm.recv(224).decode('utf-8')}")
        time.sleep(2)
        comm.send(f"I have that file will be sharing the file now".encode('utf-8'))

        file_name = str(input(f"Enter the file path/If in the same directory enter the file name: "))
        comm.send(str(file_name).encode('utf-8'))

        file_Size = os.path.getsize(file_name)
        comm.send(str(file_Size).encode('utf-8'))

        with open(file_name, 'rb') as file:
            data = file.read(file_Size)
            comm.sendall(data)
            comm.send(b"<END>")
        print("File Shared Complete")
        time.sleep(2)
        break

def make_Connection():
    pass

user = input("Lets use the Peer to Peer network\nPress Y to start\nPress N to start\n")
if user == 'N' or user == 'n':
    print("Meet you soon!")
    time.sleep(2)
    sys.exit()

elif user == 'Y' or user == 'y':
    a = enter_Host()
    b = choose_Port()
    binding(a, b)

else:
    print("Restart the program and Choose the correct option!!...")
    time.sleep(2)
    sys.exit()
