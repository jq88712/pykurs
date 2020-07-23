from sklearn import cluster
import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
import plotnine as pn
import hdbscan

data, label = make_moons(n_samples=(100, 100), noise=0.3, random_state=0)

dbscan = cluster.DBSCAN(eps=0.2)
cluster_dbscan = dbscan.fit_predict(data)

clusterer = hdbscan.HDBSCAN(min_cluster_size=10)
cluster_hdbscan = clusterer.fit_predict(data)

data_np = np.concatenate([data, cluster_dbscan.reshape(-1, 1)], axis=1)
data_df = pd.DataFrame(data_np, columns=['x', 'y', 'cluster_dbscan'])
gg = pn.ggplot(data=data_df, mapping=pn.aes(x='x', y='y', color='factor(cluster_dbscan)')) + \
     pn.geom_point()
print(gg)

data_np = np.concatenate([data, cluster_hdbscan.reshape(-1, 1)], axis=1)
data_df = pd.DataFrame(data_np, columns=['x', 'y', 'cluster_hdbscan'])
gg = pn.ggplot(data=data_df, mapping=pn.aes(x='x', y='y', color='factor(cluster_hdbscan)')) + \
     pn.geom_point()
print(gg)







