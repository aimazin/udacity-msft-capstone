*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# AutoML Time Series vs Neural Network

This Project establishes the difference between the AutoMl Time Series and Scikit Learns Neural Net on time series data.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview

'ethdata.csv' - It is Ethereum hourly financial data over about 55 days acquired by using the yahoofinance api.

### Task

The task is to predict the closing price "Close" and in AutoML the dates in "Column1".

### Access

The data will be accessed by uploading and registering the dataset in the Azure ML Workspace.

## Automated ML

Since we were time series forecasting I added the date column as a forecasting parameter and configured task to forecasting and prime metric to normalized-RMSE.

### Results

It had an RMSE of about 10 carrying a best model of StandardScalerWrapper, ELasticNet. Could have adjusted parameters for experiment to run longer for more models.

![](forpub/automldets.png)
![](forpub/automlmod.png)

## Hyperparameter Tuning

Well I used scikit-learns MLPRegressor because I thought a neuro network vs an automl would be exciting. The hyperparameters were max_iter between 100 and 1000, and epsilon between 0.0000001 and 1.0 these using a Bandit policy, Trying to minimize RMSE.

### Results

I got RMSE of less than 0.0 with hyperparameters of about 0.5 epsilon and 400 max_iter. Could have improved it by running more models only 25 were run and more hyperparameters.

![](forpub/hyptundets.png)
![](forpub/hyptunmod.png)

## Model Deployment

The deployed model is from the best registered model from the hyperdrive experiment and was deployed using the score.py file. The endpoint was consumed first of all having the raw data be present to the site as json. The requests post is used to render a response from the json uri string and header for json applications.

## Screen Recording
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

Link to a screen recording of the project in action: https://youtu.be/go4j4VXhTZw

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
