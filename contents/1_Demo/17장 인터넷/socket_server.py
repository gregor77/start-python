# -*- coding:cp949 -*- 
import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)  #������ ���� �� ���� ��ٸ���.
conn, addr = s.accept()  #������ �����Ѵ�.
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break;
    conn.send(data)   #���� �����͸� �״�� Ŭ���̾�Ʈ�� �����Ѵ�.
conn.close()
