"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 3: Estimación clorofila

@author: David Felipe Cuellar Diaz
"""

#https://https://www.indexdatabase.de/db/i-single.php?id=128
#https://www.indexdatabase.de/db/i-single.php?id=128

#NIR/GRE -1

import cv2
import numpy as np

class clorofila:
    def __init__(self,gtNIR="",maskNIR="",gtGRE="",maskGRE="",out=""):        
        self.gtNIR=gtNIR
        self.maskNIR=maskNIR
        self.gtGRE=gtGRE
        self.maskGRE=maskGRE
        self.out=out
            
    def getcl(self):
    
        imgtNIR = cv2.imread(self.gtNIR)
        immaskNIR = cv2.imread(self.maskNIR)
            
        imgtNIR = cv2.cvtColor(imgtNIR, cv2.COLOR_BGR2GRAY)
        immaskNIR = cv2.cvtColor(immaskNIR, cv2.COLOR_BGR2GRAY)
        
        sumNIR=cv2.sumElems(imgtNIR)  
        totalNIR=cv2.countNonZero(immaskNIR)  
        meanNIR=sumNIR[0]/totalNIR
        
        imgtGRE = cv2.imread(self.gtGRE)
        immaskGRE = cv2.imread(self.maskGRE)
        	
        imgtGRE = cv2.cvtColor(imgtGRE, cv2.COLOR_BGR2GRAY)
        immaskGRE = cv2.cvtColor(immaskGRE, cv2.COLOR_BGR2GRAY)
        
        sumGRE=cv2.sumElems(imgtGRE)  
        totalGRE=cv2.countNonZero(immaskGRE) 
 
        meanGRE=sumGRE[0]/totalGRE
        
        CIg=(meanNIR/meanGRE)-1	
        
        arr=np.array([[sumNIR[0],totalNIR,meanNIR],[sumGRE[0],totalGRE,meanGRE],[CIg,0,0]])
        np.savetxt(self.out + '.txt',arr,delimiter=',',fmt='%f')
        
        print("CIgreen: ", CIg)        
                
