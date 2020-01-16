import socket
import re

def connect_to_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def get_source(host, page, s):
    CRLF = '\r\n'
    request = 'GET /' + page + ' HTTP/1.1'
    request += CRLF
    request += 'Host: ' + host + CRLF
    request += CRLF

    s.sendall(str.encode(request, 'cp852'))
    return s.recv(100000).decode()

def get_images(source):
    images_list = []
    beg = 0
    while True:    
        beg_image = source.find('src="', beg)
        if beg_image == -1:
            return images_list
        end_image = source.find('"', beg_image + 5)
        image = source[beg_image + 5:end_image]
        beg = end_image + 1
        if image not in images_list:
            images_list.append(image)

s = connect_to_server("www.watchthatpage.com", 80)
source = get_source("www.watchthatpage.com", "watchPages.jsp", s)
print (source)
print (get_images(source))






    
    





"""ip = "www.tutorialspoint.com"
page = "/1280/djelatnost1280.html"
port = 80
s = connect_to_server(ip, port)
source = get_source(ip, page, s)
print (source)"""

"""
def connect_to_server(ip, port, retry = 5):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        if retry > 0:
            print (e)
            time.sleep(1)
            connect_to_server(ip, port, retry=retry-1)
    return s
    """




