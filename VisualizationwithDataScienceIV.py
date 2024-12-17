import matplotlib.pyplot as plt
import numpy as np

set1 = np.array([77, 65, 98, 23, 56, 47, 66, 22, 45, 67])

diagram, fig = plt.subplots(figsize = (10, 20))
fig.hist(set1, bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.show()