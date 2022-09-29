# Insurance Classification Case Study using Python
![](https://gifimage.net/wp-content/uploads/2018/04/learn-gif-8.gif)

The case study addreses one of the common problem in the insurance sector. To either determine the scoring as Good or bad. The decision makers rely on extensive background checks to make the decision.

AS there are many applications that come everyday , it is helpful to make a predictive model that can assist.

The below case study will discuss the step by step approach to create a machine learning predictive model in such scenarios.

Below is the procedure that was followed:

1. Reading data in the Python
2. Define the problem statement
3. Identify the target variable
4. EDA
5. Feature selection based on data distribution
6. Outlier Treatment
7. Missing value Treatment
8. Visual Correlation Analysis
9. Statistical Correlation (Feature Selection)
10. Perform One hot encoding
11. Sampling and K-fold cross validation
12. Perform classification algorithms
13. Select the best model

We shall also use stream lit to build an app that using Streamlit that will use the trained data in making prediction. Below is a look at the working of the ML work flow on StreamLit


6. Outlier Treatment
* Delete the Outlier record, only if it has few records.
* Impute the outlier values with a logical business value.

7. Missing values Treatment
If a column has more than 30% data missing, then missing value treatment cannot be done, therefore column must be rejected since too much data is missing.
## Options for missing values
* Delete the missing value rows if there are only few records exxist
* Impute the missing values with MEDIAN value for continuous variables
* Impute the missing vlaues with MODE value for the categorical values
* Interpolate the vlaues based on nearby values
* Interpolate the values based on business logic.

## Feature Selection
Best features which are correlated to the target variable. This can be done directly using correlation values or ANOVA/Chi-Square tests.

#### Visual exploration of relationship between variables
* Continuous Vs Continuous ---- Correlation matrix
* Categorical VS Continuous ---- Box Plot
* Categorical VS Categorical --- Grouped bar Plot

#### Statistical measurement of relationship between variables
* Continuous Vs Continuous ---- Correlation matrix
* Categorical Vs Continuous ---- ANOVA test
* Categorical VS Categorival ---- Chi Square test

## Implementation using Streamlit

```
pip install streamlit
streamlit run app.py

```
