import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp

x = np.linspace(0 , 2*np.pi, 100)
y = np.arctan2(x, 1)
print(y)