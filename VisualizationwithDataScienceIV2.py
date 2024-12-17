import matplotlib.pyplot as plt
import numpy as np

sugar_men = np.array([102, 90, 115, 87, 98, 100, 110])
sugar_women = np.array([89, 95, 105, 99, 84, 111, 82])

color = ["red", "blue"]

plt.xlabel("Number of People")
plt.ylabel("Glucose Level")
plt.hist([sugar_men, sugar_women], bins=[80, 90, 100, 110, 120], rwidth=0.7, label=["Men", "Women"], color=color, orientation="horizontal")
plt.title("Glucose Level in Men compared to Women")
plt.legend()
plt.show()