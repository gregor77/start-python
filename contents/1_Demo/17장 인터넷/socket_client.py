# -*- coding:cp949 -*- 
import socket

HOST = '127.0.0.1'    #localhost
PORT = 50007  #������ ���� ��Ʈ�� ����Ѵ�.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #���� ����
s.connect((HOST, PORT))
s.send(b'hello python')   #���ڸ� �����ϴ�.
data = s.recv(1024)  #������ ���� ������ �޽��ϴ�.
s.close()
print('Received', repr(data))
