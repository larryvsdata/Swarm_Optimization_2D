#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:34:02 2018

@author: ermanbekaroglu
"""

import functions2D

class objectiveFunction():
    
    def __init__(self,funct,coordinates,boundaries):
        self.funct=funct
        self.boundaryMatrix=boundaries
        self.coordinates=coordinates
        self.extraPenalty=0.0
        
    def checkBoundaries(self):
        
        boundaryPenalty=0
        for dim in range(len(self.boundaryMatrix)):
            if self.coordinates[dim]<self.boundaryMatrix[dim][0] or self.coordinates[dim]>self.boundaryMatrix[dim][1]:
                boundaryPenalty=10000
                break
                
        self.extraPenalty+=boundaryPenalty
        
    def setCoordinates(self,coordinates):
        self.coordinates=coordinates
    
    def getOF(self):
        self.checkBoundaries()
#        print('Extra penalty is: ',self.extraPenalty)
        return self.funct(self.coordinates[0],self.coordinates[1])+self.extraPenalty
    
if __name__ == "__main__":
    myFunct=functions2D.functions2D()
    myFunct.infoWrapper()
    funct=myFunct.returnTheFunction()
    
    coords=[-2.0,1.0]
    bounds=[[-10.0,10.0],[-10.0,10.0]]
    
    myOF=objectiveFunction(funct,coords,bounds)
    print(myOF.getOF())
    
    coords=[-2.0,11.0]
    myOF.setCoordinates(coords)
    print(myOF.getOF())
    
    
    
    
        
    
        
    
        
    