import socket as s
import sys
import time

HOST = s.gethostbyname(s.gethostname())
PORT = 8888
print(f"Host name IP is {HOST} and Port used is {PORT}")
time.sleep(2)

peer2 = s.socket(s.AF_INET, s.SOCK_STREAM)
peer2.connect((HOST, PORT))

while True:
    peer2.send(f"Hello, How are you?\nI need a file can you share me that file which I send you last day\n".encode('utf-8'))
    print(peer2.recv(1024).decode('utf-8'))
    time.sleep(2)

    coming_File = peer2.recv(1024).decode()
    file_Size = int(peer2.recv(1024).decode())

    with open("coming_File1.png", 'wb') as file:
        while file_Size > 0:
            data = peer2.recv(4096)
            file.write(data)
            file_Size -= len(data)

    print("File Received")
    break

sys.exit()
