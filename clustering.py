import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('trafficking.csv')

data_copy = data

columns_to_standardize = ['age', 'length']

data_copy_standardized = stats.zscore(data_copy[columns_to_standardize])

kmeans = KMeans(n_clusters=2, random_state=42).fit(data_copy_standardized)

labels = kmeans.labels_

data_copy['clusters'] = labels

columns_to_standardize.extend(['clusters'])

print(data_copy[columns_to_standardize].groupby(['clusters']).mean())

sns.lmplot('age', 'length',
			data=data_copy,
			fit_reg=False,
			hue='clusters', 
			scatter_kws={'marker': 'D', 's': 100})

plt.title('age vs length')

plt.xlabel('age')

plt.ylabel('length')

plt.show()