#-*- coding: UTF-8 -*-

'''
Created on May 7, 2018

@author: Jesús Molina
'''



class Cola(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.lista_aviones = []
    
    
    def __len__(self):
        
        return len(self.lista_aviones)
    
    
    def __str__(self): 
        
        s="Landing queue: [" 
        for x in self.lista_aviones:
            s= s + x + " ," 
        s=s.rstrip()+ "]" 
        return str(s) 
    
    def addLandingPlane(self, plane):
        
        self.lista_aviones.append(plane)
        
        
    def removeLandedPlane(self):
        
        self.lista_aviones.pop(0)