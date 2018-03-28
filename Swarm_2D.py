#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:25:46 2018

@author: ermanbekaroglu
"""
import particle2D
import functions2D
import objectiveFunction
import random as rd

class PSO_2D():
    
    def __init__(self,boundaries,noP=30,maxIter=4500,c1=2.0,c2=3.0):
        self.boundaries=boundaries
        self.dimension=2
        self.noP=noP
        self.maxIter=maxIter
        self.wMax=0.9
        self.wMin=0.2
        self.velocityConstant=0.2
        self.maxVelocities=[0.0]*self.dimension
        self.particles=[]
        self.GBESTX=[-1.0]*self.dimension
        self.GBESTO=2000000.0
        self.c1=2
        self.c2=2
        
        #Potential Function
        f_2D=functions2D.functions2D()
        f_2D.infoWrapper()
        self.myFunc=f_2D.returnTheFunction()
        
        self.OF=objectiveFunction.objectiveFunction(self.myFunc,[1.0]*self.dimension,self.boundaries)
        #Max, Min velocities
        for ii in range(self.dimension):
            self.maxVelocities[ii]=self.velocityConstant*(self.boundaries[ii][1]-self.boundaries[ii][0])
            
        self.minVelocities= [0.0]*self.dimension
        
        for ii in range(self.dimension):
            self.minVelocities[ii]=-self.velocityConstant*(self.boundaries[ii][1]-self.boundaries[ii][0])
            
        # Initialize particles
        
        for k in range(self.noP):
            self.particles.append(particle2D.particle2D())
        
        for particle in self.particles:
            for dim in range(self.dimension):
                particle.setOneCoordinate(dim,bounds[dim][0]+rd.random()*(bounds[dim][1]-bounds[dim][0]))
                
    def printParticles(self):
        
        particleNumber=0
        for particle in self.particles:
            print('Particle #',particleNumber)
            print('Location', particle.getCoordinates())
            print('Velocity', particle.getVelocities())
            print('Value', particle.getPBO())
            print('Best Location', particle.getPBX())
            particleNumber+=1
            
            
    def updateParticleBest(self,particle,currentX,currentO):
        if currentO<particle.getPBO():
            particle.setPBO(currentO)
            particle.setPBX(currentX)
            
    def updateGB(self,currentX,currentO):
        if currentO<self.GBESTO:
            print('Global value was: ',self.GBESTO)
            print('Old coordinates: ',self.GBESTX)
            self.GBESTO=currentO
            self.GBESTX=currentX
            print('New global value : ',self.GBESTO)
            print('New coordinates: ',self.GBESTX)
            print('$$$$$$$$$$$$$$$$$')
    def updateOV(self):
        particleNumber=0
        for particle in self.particles:
            currentX=particle.getCoordinates()
            self.OF.setCoordinates(currentX)
            currentO=self.OF.getOF()
#            print('Particle #',particleNumber)
#            print('Location', particle.getCoordinates())
#            print('POF', currentO)
           
#            particleNumber+=1
            self.updateParticleBest(particle,currentX,currentO)
            self.updateGB(currentX,currentO)
            
    def fixVelocities(self,particle):
        velocities=particle.getVelocities()
        
        for dim in range(self.dimension):
            if velocities[dim]>self.maxVelocities[dim]:
#                print(dim,velocities[dim],self.maxVelocities[dim] )
                particle.setOneVelocity(dim,self.maxVelocities[dim])
#                print(particle.getOneVelocity(dim))
            elif velocities[dim]<self.minVelocities[dim]:
#                print(dim,velocities[dim],self.minVelocities[dim] )
                particle.setOneVelocity(dim,self.minVelocities[dim])
#                print(particle.getOneVelocity(dim))
                
                
    def fixCoordinates(self,particle):
        coordinates=particle.getCoordinates()
        
        for dim in range(self.dimension):
            if coordinates[dim]>self.boundaries[dim][1]:
                particle.setOneCoordinate(dim,self.boundaries[dim][1])
            elif coordinates[dim]<self.boundaries[dim][0]:
                particle.setOneCoordinate(dim,self.boundaries[dim][0])
                
            
    def updateXandV(self,t):
         w=self.wMax- 1.0 * t * ((self.wMax-self.wMin)/self.maxIter)
         number=0
         for particle in self.particles:
            number+=1
            for dim in range(self.dimension):
                newVelocity=w*particle.getOneVelocity(dim)+self.c1*rd.random()*(particle.getOnePBX(dim)-particle.getOneCoordinate(dim)) \
                +self.c2*rd.random()*(self.GBESTX[dim]-particle.getOneCoordinate(dim))
                particle.setOneVelocity(dim,newVelocity)
                self.fixVelocities(particle)
                particle.setOneCoordinate(dim,particle.getOneCoordinate(dim)+newVelocity)
                self.fixCoordinates(particle)
#                if number==11:
#                    print('Location', particle.getCoordinates())
#                    print('Value', particle.getPBO())
#                    print('Best Global Location', self.GBESTX)
#                    print('%%%%%%%%%%%%%%')
#         
                
    def mainLoop(self):
        for t in range(self.maxIter):
            self.updateOV()
            self.updateXandV(t)
#            print('Iteration number: ',t)
#            print('Global Best Value: ',self.GBESTO)
#            print('Global best coordinates: ', self.GBESTX)
#            print('@@@@@@@@@@@@@@@@@@@@@')
#        
        
        
if __name__ == "__main__":
    bounds=[[-10.0,10.0],[-10.0,10.0]]
    
    swarm1=PSO_2D(bounds)
#    swarm1.printParticles()
    
    swarm1.mainLoop()
#    swarm1.printParticles()
        
        
        