# -*- coding: cp949 -*-
class GString:
    def __init__(self, init=None):
        self.content = init 
        
    def __sub__(self, str):  # '-'������ �ߺ� 
        print("- operator is called!")
    
    def __isub__(self, str): # '-='������ �ߺ�
        print("-= operator is called!")
    
g = GString("aBcdef")
g - "a"
g -= "a" 
    
