import socket

def start_server():
    s = socket.socket()
    s.bind(('127.0.0.1', 8000))
    s.listen(5)
    return s

s = start_server()

while True:
    c, adr = s.accept()
    print (c.recv(1024).decode())

    body = '<html><body><h1>Hello World!!!</h1><body></html>'
    CRLF = "\r\n"
    response = 'HTTP/1.1 200 OK' + CRLF
    response += CRLF
    response += body
    c.sendall(str.encode(response))
    c.close()













