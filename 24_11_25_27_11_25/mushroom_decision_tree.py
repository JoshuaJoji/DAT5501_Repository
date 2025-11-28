import matplotlib.pyplot as plt
import ssl
import certifi
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from ucimlrepo import fetch_ucirepo

# fetch dataset
mushroom = fetch_ucirepo(id=73)

# data (as pandas dataframes)
x = mushroom.data.features.copy()
y = mushroom.data.targets["poisonous"]

# encode categorical variables
encoding_map = {
    "a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,
    "l": 12, "m": 13, "n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,
    "v": 22,"w": 23,"x": 24,"y": 25,"z": 26,"?": 0,
}
x.replace(encoding_map, inplace=True)

# metadata
print(mushroom.metadata)

# variable information
print(mushroom.variables)

# show first 5 rows of features and target
print("\nFirst 5 rows of features (X):")
print(x.head())
print("\nFirst 5 rows of target (y):")
print(y.head())

# display settings
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)

# train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0, stratify=y
)
# train decision tree classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(x_train, y_train)
preds = clf.predict(x_test)
print("test accuracy:", accuracy_score(y_test, preds))

# Plot decision tree
plt.figure(figsize=(20, 10))
plot_tree(
    clf,
    feature_names=x.columns,
    class_names=sorted(y.unique()),
    filled=True,
)
plt.tight_layout()
plt.show()