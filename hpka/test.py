import psi4 #as psi4
import numpy as np

psi4.set_output_file("output.dat", True)
psi4.set_memory('500 MB')
numpy_memory = 2

h2o = psi4.geometry("""
O 0.0 0.0 0.0
H 1.0 0.0 0.0
H 0.0 1.0 0.0
symmetry c1
""")

#psi4.set_options({'basis': 'cc-pcdz'})
psi4.energy('scf/cc-pvdz', molecule=h2o)
psi4.optimize('scf/cc-pvdz', molecule=h2o)

scf_e, scf_wfn = psi4.frequency('scf/cc-pvdz', molecule=h2o, return_wfn=True, dertype=1)
