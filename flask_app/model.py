import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
from scipy.stats import randint, uniform
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv('data/kc_house_data.csv')

df = df[(df['price'] >= np.percentile(df['price'], 0.5)) & 
        (df['price'] <= np.percentile(df['price'], 99.5))]

# split train/test, 2015-03-01 기준으로 나눕니다
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
cutoff = pd.to_datetime('2015-03-01')
train = df[df['date'] < cutoff]
test  = df[df['date'] >= cutoff]

features = ['bedrooms', 'bathrooms', 'floors', 'sqft_living']
target = 'price'
X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

param_distributions = { 
    'n_estimators': randint(50, 500), 
    'max_depth': [5, 10, 15, 20, None], 
    'max_features': uniform(0, 1), 
}

search = RandomizedSearchCV(
    RandomForestRegressor(random_state=2), 
    param_distributions=param_distributions, 
    n_iter=5, 
    cv=3, 
    scoring='neg_mean_absolute_error', 
    verbose=10, 
    return_train_score=True, 
    n_jobs=-1, 
    random_state=2
)

search.fit(X_train, y_train);

print('최적 하이퍼파라미터: ', search.best_params_)
print('CV MAE: ', -search.best_score_)
model = search.best_estimator_

# 최적 하이퍼파라미터:  {'max_depth': 5, 'max_features': 0.18508207817320688, 'n_estimators': 122}
# CV MAE:  154721.3911233797

# pickle.dump(model, open('model/kc.pkl','wb'))

# salary_model = LinearRegression()
# salary_model.fit(X_train, y_train)

y_pred = model.predict(X_test)

pickle.dump(model, open('model/house_model.pkl','wb'))