from sklearn.neural_network import MLPRegressor
import argparse
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
import os
from azureml.core.run import Run
import pandas as pd
from azureml.core import Dataset
run = Run.get_context()



def train_test_split(data,perc):
    # Splitting series data by percentage
    data = data.values
    n = int(len(data)*(1-perc))
    return data[:n], data[n:]

def main():



    # Add arguments to script
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data',type=str)
    parser.add_argument('--epsilon',type=float, default=1e-8, help="Exploration vs Consolidation")
    parser.add_argument('--max_iter',type=int, default=200, help="Maximum number of iterations to converge")
    args = parser.parse_args()



    ws=run.experiment.workspace

    # Get the dataset from run inputs
    ds=Dataset.get_by_id(ws,id=args.input_data).to_pandas_dataframe()
    
    # Data preprocessing for training
    ds = ds[['Close']]
    
    ds['Target'] = ds.Close.shift(-1)
    
    ds = ds.dropna(axis=0)
    
    # Split data into train and test sets: 20% of the dataset to include in the test split.
    train, test = train_test_split(ds, 0.2)
    
    x_train = train[:,:-1]
    x_test = test[:,:-1]
    y_train = train[:,-1]
    y_test = test[:,-1]


    run.log("Epsilon:", np.float(args.epsilon))
    run.log("Max iterations:", np.int(args.max_iter))

    # Model training and evaluation
    model = MLPRegressor(epsilon=args.epsilon, max_iter=args.max_iter).fit(x_train, y_train)
    pred = model.predict(x_test)
    mse = mean_squared_error(x_test, pred)
    rmse = np.sqrt(mse)
    acc = model.score(x_test, y_test)
    run.log("RMSE", np.float(rmse))
    run.log("Accuracy", np.float(acc))
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/hyptun_model.joblib')



    

if __name__ == '__main__':
    main()
