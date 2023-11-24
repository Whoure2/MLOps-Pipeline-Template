import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def prepare_dataset(file_path, target_col):
    df = pd.read_csv(file_path)
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test
\n# Maintenance log 1\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 5\n# Maintenance log 6\n# Maintenance log 8\n# Maintenance log 9\n# Maintenance log 11\n# Maintenance log 12\n# Maintenance log 13\n# Maintenance log 14\n# Maintenance log 15\n# Maintenance log 16\n# Maintenance log 18\n# Maintenance log 19\n# Maintenance log 20\n# Maintenance log 21\n# Maintenance log 22\n# Maintenance log 23\n# Maintenance log 25\n# Maintenance log 26\n# Maintenance log 29