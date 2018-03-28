#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:25:00 2018

@author: ermanbekaroglu
"""

class particle2D():

    
    def __init__(self):
        self.dimension=2
        self.verbose=False
        self.coordinates=[0.0]*self.dimension
        self.velocities=[0.0]*self.dimension
        self.PBO=1000000.0
        self.PBX=[0.0]*self.dimension
        
    def setPBX(self,PBX):
        self.PBX=PBX
        
        
    def setCoordinates(self,coord):
        self.coordinates= coord
        
    def setVelocities(self,vs):
        self.velocities= vs
        
    def setPBO(self,PBO):
        self.PBO=PBO
        
    def setOnePBX(self,dimension,PBX):
        self.PBX[dimension]=PBX[dimension]
        
    def setOneCoordinate(self,dimension,coord):
        self.coordinates[dimension]=coord
        
    def setOneVelocity(self,dimension,velocity):
        self.velocities[dimension]=velocity
        
    def getCoordinates(self):
        return self.coordinates
        
    def getVelocities(self):
        return self.velocities
        
    def getPBO(self):
        return self.PBO
    
    def getPBX(self):
        return self.PBX
    
    def getOnePBX(self,dimension):
        return self.PBX[dimension]
        
    def getOneCoordinate(self,dimension):
        return self.coordinates[dimension]
        
    def getOneVelocity(self,dimension):
        return self.velocities[dimension]
    
    def moveOneCoordinate(self,dimension,velocity):
        self.coordinates[dimension]+=velocity
        
    def moveAll(self,velocities):
        self.coordinates+=velocities
        
if __name__ == "__main__":
    myParticle=particle2D()
    myParticle.setCoordinates([2.0,1.0])
    print(myParticle.getCoordinates())
    myParticle.setOneCoordinate(1,33.0)
    print(myParticle.getCoordinates())
    myParticle.moveOneCoordinate(1,3)
    print(myParticle.getCoordinates())
    myParticle.setVelocities([21.0,13.0])
    print(myParticle.getVelocities())
    myParticle.setOneVelocity(0,41.0)
    print(myParticle.getVelocities())
    
        
        
        
        