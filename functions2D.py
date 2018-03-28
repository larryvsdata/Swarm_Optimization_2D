#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:08:49 2018

@author: ermanbekaroglu
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def styblinski(x,y):
        return(1.0/2*(x**4-16*x**2+5*x+y**4-16*y**2+5*y))
    
def ackley2d(x, y, a=20, b=0.2, c=2*np.pi):
        d = 2
        sum1 = x**2 + y**2
        sum2 = np.cos(c*x) + np.cos(c*y)
        term1 = -a * np.exp(-b*np.sqrt(sum1/d))
        term2 = -np.exp(sum2/d)
        s = term1 + term2 + a + np.exp(1)
        return(s)
        
def eggholder(x, y):
        return(-(y + 47)*np.sin(np.sqrt(np.abs(y+x/2+47))) - x*np.sin(np.sqrt(np.abs(x - (y+47)))))
    
    
def dropWave(x, y):
        frac1 = 1 + np.cos(12*np.sqrt(x**2+y**2));
        frac2 = 0.5*(x**2+y**2) + 2;
    
        return -frac1/frac2  
    
    
def holder(x, y):
        fact1 = np.sin(x)*np.cos(y);
        fact2 = np.exp(np.abs(1 - np.sqrt(x**2+y**2)/np.pi));
    
    
        return -np.abs(fact1*fact2) 
    
def booth(x, y):
        term1 = (x + 2*y - 7)**2;
        term2 = (2*x + y - 5)**2;
    
    
        return term1 + term2 
    
def camel(x,y):
        term1 = 2*x**2;
        term2 = -1.05*x**4;
        term3 = x**6 / 6;
        term4 = x*y;
        term5 = y**2;
        
        return  term1 + term2 + term3 + term4 + term5;
    
    
def camel6(x,y):
        term1 = (4-2.1*x**2+(x**4)/3) * x**2;
        term2 = x*y
        term3 = (-4+4*y**2) * y**2
    
        
        return  term1 + term2 + term3 ;
    
    
def plot2D(xlinStart,xlinEnd,ylinStart,ylinEnd,xPoints,yPoints,funct):
        fig=plt.figure(figsize=(10,7))
        ax=fig.gca(projection='3d')
        x=np.linspace(xlinStart,xlinEnd,xPoints)
        y=np.linspace(ylinStart,ylinEnd,yPoints)
        X,Y=np.meshgrid(x,y)
        Z=funct(X,Y)
        
        surf=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.cm.coolwarm,linewidth=0,antialiased=False)
        ax.zaxis.set_major_locator(plt.LinearLocator(10))
        ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))
    
        plt.tick_params(axis='both',which='major',labelsize=8)
        ax.tick_params(labelsize=8)
    
        fig.colorbar(surf,shrink=0.5,aspect=7,cmap=plt.cm.coolwarm)
    
        plt.show()

    




class functions2D():

    
    def __init__(self):
        
        self.functionList=[styblinski,ackley2d,eggholder,dropWave,holder,booth,camel,camel6]
        self.functionNameDict={}
        self.function=styblinski
        
        
    def createFunctionNameDict(self):
        
        for ii in range(len(self.functionList)):
            self.functionNameDict[ii]=self.functionList[ii]
    
    def printFunctionNames(self):
        
        for functionName in self.functionNameDict:
            print(functionName,self.functionNameDict[functionName].__name__)
            
    def getTheFunction(self):

        number=input('Enter the function number: \n')
        number=int(number)
        self.function=self.functionNameDict[number]
        
    def plotFunction(self):
        plot2D(-5.0,5.0,-5.0,5.0,50,50,self.function)
        
    def returnTheFunction(self):
        return self.function
    
    def infoWrapper(self):
        self.createFunctionNameDict()
        self.printFunctionNames()
        self.getTheFunction()
        self.plotFunction()
        
        
            
            
if __name__ == "__main__":
    myFunctions=functions2D()
    myFunctions.infoWrapper()

        
            
        
        
        
        
        
        
        
