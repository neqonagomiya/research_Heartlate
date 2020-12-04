import pandas as pd
import matplotlib.pyplot as plt

filename = input("filename.csv->")
df = pd.read_csv(filename, header=None)

plt.plot(df)
plt.show()
