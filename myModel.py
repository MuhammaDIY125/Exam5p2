import joblib
from sklearn.ensemble import RandomForestRegressor
from myDatasets import X, y

SEED = 1

rf_model = RandomForestRegressor(
    n_estimators=336,
    criterion='absolute_error',
    max_depth=6,
    min_samples_split=7,
    min_samples_leaf=7,
    min_impurity_decrease=0.07835,
    ccp_alpha=0.05618,
    n_jobs=-1,
    random_state=SEED
)

rf_model.fit(X, y)

joblib.dump(rf_model, 'rf_model.pkl')