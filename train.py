from sklearn.neural_network import MLPClassifier
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd



def main():
    run = Run.get_context()



    parser = argparse.ArgumentParser()
    parser.add_argument('--epsilon',type=float, default=1e-8, help="Exploration vs Consolidation")
    parser.add_argument('--max_iter',type=int, default=200, help="Maximum number of iterations to converge")
    args = parser.parse_args()




    ds = run.input_datasets['gas']



    x, y = ds.loc['time'], ds.loc['R7']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2020)



    run.log("Epsilon:", np.float(args.epsilon))
    run.log("Max iterations:", np.int(args.max_iter))

    model = MLPClassifier(epsilon=args.epsilon, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    joblib.dump(value=model, filename='outputs/hyptun_model.joblib')



    run.complete()

if __name__ == '__main__':
    main()