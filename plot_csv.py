import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Ardu_heart.csv", header=None)

plt.plot(df)
plt.show()
