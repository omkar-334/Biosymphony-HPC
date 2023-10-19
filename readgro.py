import numpy as np
import linecache as lc
title=lc.getline('equilibration.gro',1).strip()
atoms=lc.getline('equilibration.gro',2).strip()
vectors=open('equilibration.gro','r').readlines()[-1].strip()
data = np.loadtxt(open('equilibration.gro','r').readlines()[:-1],skiprows=2,dtype=str)
print(title)
print(atoms)
print(vectors)
print(data)