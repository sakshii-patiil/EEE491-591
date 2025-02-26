#Problem 1

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("heart1.csv")

# Display basic info and statistics
print("Dataset Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Compute the correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Compute the covariance matrix
covariance_matrix = df.cov()
print("\nCovariance Matrix:")
print(covariance_matrix)

# Identify highly correlated features
high_corr = correlation_matrix[abs(correlation_matrix) > 0.5]
print("\nHighly Correlated Features:")
print(high_corr)

# Generate a pair plot
sns.pairplot(df, diag_kind='kde')
plt.show()

# Observations based on analysis
observations = """
Key Observations:
- Certain features show strong correlations, which may impact model performance.
- The covariance matrix suggests dependencies between features.
- Pair plots reveal potential relationships in the dataset.
- Further processing may be required before training models.
"""
print(observations)