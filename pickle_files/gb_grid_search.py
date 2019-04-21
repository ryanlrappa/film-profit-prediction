import pickle
import pandas as pd 
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, GridSearchCV

df = pd.read_csv('/home/ubuntu/clean_data_v3.csv')

cols_X = ['budget', 
          'runtime', 
          'releases', 
          'cast_rev', 
          'cast_prof', 
          'cast_films', 
          'cast_prof_films', 
          'dir_rev',
          'dir_prof', 
          'dir_films', 
          'dir_prof_films', 
          'writ_rev', 
          'writ_prof', 
          'writ_films', 
          'writ_prof_films', 
          'adj_budget',
          'cast_dir_avg_rev',
          'fall', 'spring', 'summer', 'winter',
          'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'None', 'Romance', 'Science Fiction', 'Thriller', 'War', 'Western',
          'compet_cast_rev', 'compet_cast_prof', 'compet_cast_films', 'compet_cast_prof_films', 'compet_dir_rev', 'compet_dir_prof', 'compet_dir_films', 'compet_dir_prof_films', 'compet_writ_rev', 'compet_writ_prof', 'compet_writ_films', 'compet_writ_prof_films', 
          'compet_budget',
          'compet_adj_budget',
          'compet_cast_dir_avg_rev']

col_y = ['made_money']

X = df.loc[:, cols_X].values
y = df.loc[:, col_y].values.ravel()

print(X.shape)
print(y.shape)

scaler = StandardScaler()
skf = StratifiedKFold(n_splits = 5, shuffle = True, random_state=313)
for train_index, test_index in skf.split(X, y):
    X_train_scaled, y_train = scaler.fit(X[train_index]).transform(X[train_index]), y[train_index]
    X_test_scaled, y_test = scaler.fit(X[test_index]).transform(X[test_index]), y[test_index]
    break
    
parameters = {
    "learning_rate": [0.1],  #lower and graph this later
    "min_samples_split": np.linspace(0.1, 0.5, 5),
    "min_samples_leaf": np.linspace(0.1, 0.5, 5),
    "max_depth":[3,5,8],
    "max_features":["log2","sqrt"],
    "criterion": ["friedman_mse",  "mae"],
    "subsample":[0.6, 0.7, 0.8, 0.9, 1.0],
    "n_estimators":[500]  #lower and graph this later
    }

clf = GridSearchCV(GradientBoostingClassifier(), parameters, cv=10, n_jobs=-1)

print("Grid search in progress...")

clf.fit(X_train_scaled, y_train)

print("Grid search complete.")

pickle_out = open("gbc.pkl","wb")
pickle.dump(clf, pickle_out)
pickle_out.close()

print("Pickle complete.")
