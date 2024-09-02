import pandas as pd

# Reading the data
data = pd.read_csv('Diabetes_data.csv')

# The Id Column is just an identification to each unique data that was collected so it is now of no use
data.drop('Id',axis=1, inplace=True)

X = data.drop('Outcome', axis=1)
y = data.Outcome

from sklearn.model_selection import train_test_split # libraries to split the data into testing and training set

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.73, random_state=17)
from sklearn.ensemble import RandomForestClassifier
forest_model = RandomForestClassifier(n_estimators=237)
forest_model.fit(X_train, y_train)

# importing pickle for saving and loading to be certain it works
from pickle import dump, load

# Saving... to a binary file in .pkl extension
with open('Diabetes saved.pkl', 'wb') as mod:
    dump(forest_model, mod)
    print('Done')
