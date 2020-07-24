import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.metrics import f1_score, r2_score
import plotnine as pn

classifier = SVC(gamma=2, C=1)

data, label = make_moons(n_samples=(100, 100), noise=0.3, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=.3, random_state=42)





classifier.fit(X_train, y_train)

y_test_pred = classifier.predict(X_test)

score = classifier.score(X_test, y_test)
score = np.mean(y_test_pred == y_test)

f1_score(y_test, y_test_pred)

# np.concatenate([data, label.ndmin(1, -1)], axis=1)
# np.concatenate([data, label.reshape(110, 1)], axis=1)
# np.concatenate([data, label.reshape(label.shape[0], 1)], axis=1)

data_train_np = np.concatenate([data, label.reshape(-1, 1)], axis=1)
data_train_df = pd.DataFrame(data_train_np, columns=['x', 'y', 'label'])
gg1 = pn.ggplot(data=data_train_df, mapping=pn.aes(x='x', y='y', color='factor(label)')) + \
    pn.geom_point()
print(gg1)

y_pred = classifier.predict(data)
col = np.array([(j if i else -1) for i, j in zip(list(y_pred == label), list(label))])
data_train_np = np.concatenate([data, col.reshape(-1, 1)], axis=1)
data_train_df = pd.DataFrame(data_train_np, columns=['x', 'y', 'col'])
gg2 = pn.ggplot(data=data_train_df, mapping=pn.aes(x='x', y='y', color='factor(col)')) + \
     pn.geom_point()
print(gg2)
