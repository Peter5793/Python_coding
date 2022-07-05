## Bank Churn Rates

Customer churn rate is better known as customer attrition rate and measures the proportion of contractural customers of ca company who ceasei their supscription over a defiend time period. Some examples include :
1. Streaming service i.e. netflix, Disney+ and Showmax
2. Spotify etc

![churn_rate](https://cdn.corporatefinanceinstitute.com/assets/churn-rate-1024x683.jpeg)

### Importance 
For any critical business metric that runs on a subscription based model , having a very high churn rate can be detrimental in terms of profitability and its overal existance.

Having a preditive model to predict chrun rate can help forecast such rates and also look  at what are the major variables that affect them.

## Goal

The notebook is aimed at utilizing python at predicting the churn rate for a banking institution in different sectors.

## Method
the main method used in this notebook was through random forest classification.
This was due to the binary nature of the target variable. The answer is binary in nature 0 or 1.

1. Import Libraries
2. Load data
3. Perform EDA
4. Split the data into training and test sets
5. Train the ML algorithm
6. Model Evaluation
7. Feature Evalution (using Random forest attribute feature importance)

### Summary
As a result of using this algorithm, we had a prediction score of 86.95%. Therefore, predicts churn by 86.95%.

![results](./Screenshot%202022-04-28%20115259.png)