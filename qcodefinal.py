import numpy as np
from qutip import Bloch
import matplotlib.pyplot as plt


theta = np.deg2rad(135)  
phi = np.deg2rad(0)    


bloch = Bloch()


x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)


bloch.add_vectors([x, y, z])


bloch.render()


plt.show()
