#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:38:14 2018

@author: arpanganguli
"""

# import statistical tools
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor

# import data visualisation tools
import matplotlib.pyplot as plt
import seaborn as sns

# load data; visualisation same as Section 3.6.3
url = "/Users/arpanganguli/Documents/Finance : ML/ISLR/Datasets/Boston.csv"
Boston = pd.read_csv(url, index_col = 'Unnamed: 0')

# perform regression without transformation
Y = Boston['medv']
X1 = Boston['lstat']
model1 = ols('Y~X1+X2(X1)', data = Boston).fit()
print(model1.summary())

# perform regression with transformation
X2 = lambda X1 : pow(X1,2) # X2 is a lambda function that raises each element of X1 to the power of 2
model2 = ols('Y~X1+X2(X1)', data = Boston).fit()
print(model2.summary())

# perform anova between model1 and model2
anova_table = sm.stats.anova_lm(model1, model2) # results not ideal. Need to refine this
print(anova_table)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RESULTS (NOT PART OF CODE)

runfile('/Users/arpanganguli/Documents/Finance : ML/ISLR/Codes - Python/Section3.6.5.py', wdir='/Users/arpanganguli/Documents/Finance : ML/ISLR/Codes - Python')
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      Y   R-squared:                       0.641
Model:                            OLS   Adj. R-squared:                  0.639
Method:                 Least Squares   F-statistic:                     448.5
Date:                Thu, 27 Dec 2018   Prob (F-statistic):          1.56e-112
Time:                        20:32:12   Log-Likelihood:                -1581.3
No. Observations:                 506   AIC:                             3169.
Df Residuals:                     503   BIC:                             3181.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     42.8620      0.872     49.149      0.000      41.149      44.575
X1            -2.3328      0.124    -18.843      0.000      -2.576      -2.090
X2(X1)         0.0435      0.004     11.628      0.000       0.036       0.051
==============================================================================
Omnibus:                      107.006   Durbin-Watson:                   0.921
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              228.388
Skew:                           1.128   Prob(JB):                     2.55e-50
Kurtosis:                       5.397   Cond. No.                     1.13e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.13e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      Y   R-squared:                       0.641
Model:                            OLS   Adj. R-squared:                  0.639
Method:                 Least Squares   F-statistic:                     448.5
Date:                Thu, 27 Dec 2018   Prob (F-statistic):          1.56e-112
Time:                        20:32:12   Log-Likelihood:                -1581.3
No. Observations:                 506   AIC:                             3169.
Df Residuals:                     503   BIC:                             3181.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     42.8620      0.872     49.149      0.000      41.149      44.575
X1            -2.3328      0.124    -18.843      0.000      -2.576      -2.090
X2(X1)         0.0435      0.004     11.628      0.000       0.036       0.051
==============================================================================
Omnibus:                      107.006   Durbin-Watson:                   0.921
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              228.388
Skew:                           1.128   Prob(JB):                     2.55e-50
Kurtosis:                       5.397   Cond. No.                     1.13e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.13e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
   df_resid           ssr  df_diff  ss_diff   F  Pr(>F)
0     503.0  15347.243158      0.0      NaN NaN     NaN
1     503.0  15347.243158     -0.0     -0.0 NaN     NaN
