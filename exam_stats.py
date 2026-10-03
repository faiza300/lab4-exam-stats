import pandas as pd
import numpy as np
from scipy import stats

scores = pd.Series([72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69])

print(scores.describe())

clean = scores.dropna()
print("Skewness:", stats.skew(clean))
print("Kurtosis:", stats.kurtosis(clean))

print("Missing values:", scores.isnull().sum())

filled = scores.fillna(scores.mean())
print("Filled scores:")
print(filled)
