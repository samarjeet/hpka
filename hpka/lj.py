import psi4
import numpy as np

psi4.set_memory("500 MB")
he_dimer = """
He
--
He 1 **R**
"""

distances = [2.875, 3.0, 31.125, 3.25, 3.375, 3.5, 3.75, 4.0, 4.5, 5.0, 6.0, 7.0]

energies = []

for d in distances :
  mol = psi4.geometry(he_dimer.replace('**R**', str(d)))

  en = psi4.energy('MP2/aug-cc-pVDZ', molecule=mol, bsse_type='cp')

  en *= 219474.6

  energies.append(en)

print("Finished computing the potentials")
