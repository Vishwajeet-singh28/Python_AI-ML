import matplotlib.pyplot as plt
import numpy as np

y=np.array([80,125,120,115,95,90,105,85,100,110])
x=np.array([240,250,260,270,280,290,300,310,320,330])
plt.title("sports watch data")
plt.xlabel("calorie burnage")
plt.ylabel("average pulse")
plt.plot(x,y)
plt.show()
