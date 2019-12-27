"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Test - estimación clorofila

@author: David Felipe Cuellar Diaz
"""

import clorofila

folderin = "/home/tg1907/Documents/Tesis5/clases/images/"

fr=9
to=9

while fr <= to:
	
    print(fr)
    
    gtNIR= folderin + str(fr) + "/NIR/guided/imagegf.bmp"
   
    maskNIR= folderin + str(fr) + "/NIR/guided/maskotsu.bmp"

    gtGRE= folderin + str(fr) + "/GRE/guided/imagegf.bmp"
   
    maskGRE= folderin + str(fr) + "/GRE/guided/maskotsu.bmp"

    out= folderin + "clorofila/" + "cig_" + str(fr)

    cvi=clorofila.clorofila(gtNIR=gtNIR,maskNIR=maskNIR,gtGRE=gtGRE,maskGRE=maskGRE,out=out)
    

    cvi.getcl()
    
    fr = fr+1

    
