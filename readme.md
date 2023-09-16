# Peer-to-Peer Network File Sharing

This simple Python program allows two peers to share files over a local network.

## Peer 1

### How to Run Peer 1

1. Open a terminal.
2. Navigate to the directory containing `peer1.py`.
3. Run the script using Python:

```bash
python peer1.py
```

### Steps

1. **Enter Host Name**

   - You will be prompted to enter the host name. Follow these steps if you're unsure:

      - Open CMD/terminal.
      - Type `ipconfig`.
      - Locate the Ethernet/Wifi IPv4 address.

2. **Choose Port Number**

   - Enter a port number between 3000 to 65535.

3. **Binding**

   - The program will bind to the specified host and port.

4. **Connection**

   - Peer 1 will wait for a connection from Peer 2.

5. **File Sharing**

   - You'll be prompted to enter the file path. If the file is in the same directory, just enter the file name.

6. **File Transfer**

   - The file will be sent to Peer 2.

## Peer 2

Peer 2 acts as the client.

### How to Run Peer 2

1. Open a terminal.
2. Navigate to the directory containing `peer2.py`.
3. Run the script using Python:

```bash
python peer2.py
```

### Steps

1. **Host Name and Port**

   - Peer 2 will connect to Peer 1 using the specified host name and port (provided by Peer 1).

2. **File Request**

   - Peer 2 will send a message to request the file.

3. **File Receiving**

   - The file will be received and saved as `coming_File1.png`.

 **Reference**

   - https://docs.python.org/3/library/socket.html
   - https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python
   - https://www.youtube.com/watch?v=YwWfKitB8aA
   - https://krishisanskriti.org/vol_image/02Jul201506073518.pdf
   - https://www.youtube.com/playlist?list=PLS1QulWo1RIZGSgRsn0b8w9uoWM1gHDpo
   - https://medium.com/@luishrsoares/implementing-peer-to-peer-data-exchange-in-python-8e69513489af


---
