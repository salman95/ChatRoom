# ChatRoom

For this project, I created a chat room system that reads the inputs from the clients and sends the data to the server program.  The server program then takes the data and sends it back to all connected clients for them to interact with each other. The server acts as a centralized location to route data from one client to another. The clients are needed for the users to create data and communicate with each other. Each client that is connected will create a new thread in the server and each thread is treated as a client. 

The program was created in Python, as stated in the requirements. The version I used was Python 3.6. It provided me with the Python socket library, which was needed for the server and clients to communicate. I also imported from the “_thread” library in the server program. I only imported the “start_new_thread” function since that is what I only needed. I used it to create a new thread for each client that is connected. This lets the server connect more than one client at a time.

The way this chat room works is the traditional way of server-client communication. All data that the client types up is encoded from string to bytes. These bytes of data are then sent to the server for analyzation. From there, many things can happen. If the data is read in all capital letters, then a warning is sent to the client that sent the data. If this happens once more, the server will send a “Kick” signal to the client prompting it to break and thus disconnecting it from the server. If the data reads as “!leave”, then the “Kick” signal is sent and the client will be disconnected. If none of these are read in the encoded data, then the data will be sent to all clients that are currently connected. 

The way I tested the program is by going into the terminal and running the server and clients from there. I needed to open 2 – 4 terminal windows to test the server with a couple of clients. Since I was using Python 3.6, I ran the server as “python 3 Server.py” and the client as “python 3 Client.py”. You must open the server up first in one of the terminal windows and then the clients from the other terminal windows. I typed in the client windows to see the interaction.

**Running Server:**
![alt text](https://i.imgur.com/HdM3XRj.png)


![alt text](https://i.imgur.com/UJi5Hb0.jpg)


![alt text](https://i.imgur.com/gpKStmn.jpg)


**Kicked Client:**
![alt text](https://i.imgur.com/50KaSH4.jpg)


**Client Leaving:**
![alt text](https://i.imgur.com/0P9QcAZ.jpg)


**Server Log:**
![alt text](https://i.imgur.com/AdSEoqw.jpg)
