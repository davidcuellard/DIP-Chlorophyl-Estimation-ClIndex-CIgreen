"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Test - estimación clorofila

@author: David Felipe Cuellar Diaz
"""

import clorofila

import os
folderin = os.getcwd()

gtNIR= folderin + "/NIRgroundtruth/imagegf.bmp"

maskNIR= folderin + "/NIRgroundtruth/maskotsu.bmp"

gtGRE= folderin + "/GREgroundtruth/imagegf.bmp"

maskGRE= folderin + "/GREgroundtruth/maskotsu.bmp"

out= folderin + "/results/" + "cig"

cvi=clorofila.clorofila(gtNIR=gtNIR,maskNIR=maskNIR,gtGRE=gtGRE,maskGRE=maskGRE,out=out)


cvi.getcl()


