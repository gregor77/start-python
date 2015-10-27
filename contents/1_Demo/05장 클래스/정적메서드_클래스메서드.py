# -*- coding: cp949 -*-
class CounterManager:
    insCount = 0
    def __init__(self):
        CounterManager.insCount += 1
    def staticPrintCount():  #���� �޼��� ���� 
        print("Instance Count: ", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount) #���� �޼��� ��� 
    
    def classPrintCount(cls): #Ŭ���� �޼��� ����(�Ϲ������� ù ���ڴ� Ŭ������ ����)
        print("Instance Count: ", cls.insCount)
    CPrintCount = classmethod(classPrintCount) #Ŭ���� �޼���� ��� 
        
a, b, c = CounterManager(), CounterManager(), CounterManager()

#���� �޼���� �ν��Ͻ� ��ü ������ ��� 
CounterManager.SPrintCount()
b.SPrintCount()
#Ŭ���� �޼���� �ν��Ͻ� ��ü ������ ��� 
CounterManager.CPrintCount()
b.CPrintCount() 
