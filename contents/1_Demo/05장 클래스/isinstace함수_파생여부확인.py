#coding:utf-8
'''
Created on 2013. 12. 2.

@author: Administrator
'''
class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass
p, s = Person(), Student()
#��Ӱ��踦 �ľ��Ѵ�. 
print("p is instance of Person: ", isinstance(p, Person))
#���� 3 ���ķ� ��� Ŭ������ object���� �Ļ��� 
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))