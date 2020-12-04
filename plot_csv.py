import pandas as pd
import matplotlib.pyplot as plt

#filename = input("filename.csv->")
df = pd.read_csv("Ardu_heart5.csv", header=None)

plt.plot(df)
plt.show()
