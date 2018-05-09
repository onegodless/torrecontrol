#-*- coding: UTF-8 -*-

'''
Created on May 7, 2018

@author: Jesús Molina
'''

import random

from TADcola import Cola

from faker import Faker


class TorreDeControl(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.fake = Faker()
        self.instanceLanding = Cola()
        self.instanceTakeoff = Cola()
        
        
    def __str__(self): #Imprime el contenido de las dos colas.
    
        print self.instanceLanding
        print self.instanceTakeoff
    
        
    def addPlane(self):
                
        status = random.randint(1,2) #sets if the new plane is waiting to take-off(1) or land(2).  
        if random.randint(1,3) == 1: #1 in 3 probabilities for a new plane to appear.
            if status == 1: #the new plane wants to land.
                new_plane = self.fake.ssn() 
                self.instanceLanding.addLandingPlane(new_plane) #adds the new plane to the landing queue. fake.ssn() generates a random id for the plane.
                print 'The new spotted plane (%s) wants to land.' % (new_plane)
                print self.instanceLanding
            
            elif status == 2: #the new plane wants to take-off.
                new_plane = self.fake.ssn() 
                self.instanceTakeoff.addDepartingPlane(new_plane)
                print 'The new spotted plane (%s) wants to take-off.' % (new_plane)
                print self.instanceTakeoff 
                
            
    def permissionGiver(self):
        
        print self.instanceLanding
        print self.instanceTakeoff
        
        if len(self.instanceLanding) != 0:
                self.instanceLanding.removeLandedPlane()
                print "A plane landed."
        
        elif len(self.instanceTakeoff) != 0: #If there is no plane waiting to land, we try to make a plane take-off.
                self.instanceTakeoff.removeDepartedPlane() #Removes the plane departed.
                print "A plane departed. "
                
        else:
            print 'There are no planes waiting to land nor to take-off.'