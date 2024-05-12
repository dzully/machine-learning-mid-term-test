import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('dataset.csv')

plt.scatter(data['Flight distance'], data['Satisfaction'])
plt.xlabel('Flight Distance')
plt.ylabel('Satisfaction Level')
plt.title('Flight Distance vs. Satisfaction Level - 22050897')
plt.show()
