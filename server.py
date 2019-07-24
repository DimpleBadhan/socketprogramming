import socket


s = socket.socket()
print("Socket Created Successfully")

port = 12345

s.bind(('',port))
print("Socket binded to %s"%(port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Get connection ")
    c.send('Thank you for connecting')
    c.close()
    