import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import ParameterSampler
from src.utils import date

def main(mega_df):
    # create training and validation sets

    val_start = date.trading_sessions(back_days=63)[0]
    train_end = date.trading_sessions(back_days=85)[-1]

    train = mega_df[mega_df['Date'] < train_end]
    val = mega_df[mega_df['Date'] >= val_start]
    
    # define ML features and target

    features = [c for c in mega_df.columns if c not in ['target_daily_return', 'Date', 'ticker']]
    target = 'target_daily_return'

    # define parameter distribution

    param_dist = {
        'max_depth': [2, 3, 4, 5, 6, 8],
        'min_child_weight': [1, 2, 5, 10, 20],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0],
        'gamma': [0, 0.5, 1, 2, 5],
        'reg_alpha': [0, 0.1, 0.5, 1.0],
        'reg_lambda': [1, 2, 5, 10],
        'learning_rate': [0.01, 0.03, 0.05, 0.1, 0.2]
    }

    best = {'mae': float('inf'), 'params': None, 'model': None}

    # loop through params and test for mean average error

    for params in ParameterSampler(param_dist, n_iter=30, random_state=1):

        model = XGBRegressor(
            n_estimators=5000,
            objective='reg:squarederror',
            tree_method='hist',
            n_jobs=-1,
            **params
        )

        model.fit(
            train[features],
            train[target],
            eval_set=[(val[features], val[target])],
            callbacks=[xgb.callback.EarlyStopping(rounds=50, save_best=True)],
            verbose=False
        )

        preds = model.predict(val[features])
        mae = mean_absolute_error(val[target], preds)

        if mae < best['mae']:
            best = {'mae': mae, 'model': model, 'parameters': params}

    # return best model

    return best