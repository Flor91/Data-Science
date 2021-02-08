import os

import numpy as np

file = os.sep.join([os.getcwd(), "Data", "populations.txt"])

data = np.genfromtxt(file, delimiter="\t", skip_header=True)
print(data[:5])

year = data[:, 0]
conejos = data[:, 1]
linces = data[:, 2]
zanahorias = data[:, 3]

poblaciones = data[:, 1:]

print("        Conejos, Linces, Zanahorias")
print("Mean:", np.around(poblaciones.mean(axis=0), decimals=2))
print("Std:", np.around(poblaciones.std(axis=0), decimals=2))
