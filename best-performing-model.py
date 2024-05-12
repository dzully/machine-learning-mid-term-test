import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = pd.read_csv('dataset.csv')

sns.barplot(x='Inflight Wi-Fi service', y='Satisfaction', data=data)
plt.xlabel('Inflight WiFi Service')
plt.ylabel('Satisfaction Level')
plt.title('Inflight WiFi Service vs. Satisfaction Level - 22050897')
plt.show()
