import socket
import time
import threading
import sys

'''
example: 
ping 8.8.8.8 | python3 logger.py &
nc 127.0.0.1 6109
'''

lines_size = 4096
lines = []

def read_from_stdin():
    global lines
    while True:
        line = sys.stdin.readline()
        if line==None or len(line)==0:
            time.sleep(1)
            continue
        line = line.encode()
        while len(lines)>=lines_size:
            lines.pop(0)
        lines.append(line)
        #print(lines)

stdin_thread = threading.Thread(target=read_from_stdin)
stdin_thread.start()

tcpServerSocket=socket.socket()
host = '127.0.0.1'
port=6109
tcpServerSocket.bind((host,port))
tcpServerSocket.listen(1)
while True:
    c, addr = tcpServerSocket.accept()       
    #print ('client address:', addr)
    while True:
        if len(lines)==0:
            time.sleep(0.1)
            continue
        line=lines.pop(0)
        try:
            c.send(line)
        except Exception as e:
            #print(e)
            try:
                c.shutdown(socket.SHUT_WR)
            except Exception as e:
                #print(e)
                pass
            c.close()
            break
