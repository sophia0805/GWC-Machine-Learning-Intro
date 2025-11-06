import pandas as pd
import GWCutilities as util
import sys
import os

# Handle bundled data file path for PyInstaller
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

print("\n-----\n")

#Create a variable to read the dataset
df = pd.read_csv(resource_path("heartDisease_2020_sampling.csv"))

print(
    "We will be performing data analysis on this Indicators of Heart Disease Dataset. Here is a sample of it: \n"
)

#Print the dataset's first five rows
print(df.head())

input("\n Press Enter to continue.\n")



#Data Cleaning
#Label encode the dataset
df = util.labelEncoder(df, ["HeartDisease", "Smoking", "AlcoholDrinking", "Sex", "AgeCategory", "PhysicalActivity", "GenHealth"])

print("\nHere is a preview of the dataset after label encoding. \n")
print(df.head())

input("\nPress Enter to continue.\n")

#One hot encode the dataset
df = util.oneHotEncoder(df, ["Race"]) 

print(
    "\nHere is a preview of the dataset after one hot encoding. This will be the dataset used for data analysis: \n"
)
print(df.head())

input("\nPress Enter to continue.\n")


#Creates and trains Decision Tree Model
from sklearn.model_selection import train_test_split
X = df.drop("HeartDisease", axis = 1)
y = df["HeartDisease"]
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 1) 


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)


#Test the model with the testing data set and prints accuracy score
test_predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score

test_acc = accuracy_score(y_test, test_predictions)

print("The accuracy with the testing dataset of the decision tree is: " + str(test_acc))
#Prints the confusion matrix
from sklearn.metrics import confusion_matrix


cm = confusion_matrix(y_test, test_predictions, labels = [1,0])
print("The confusion matrix of the tree is: " + str(cm))


#Test the model with the training data set and prints accuracy score
train_predictions = clf.predict(X_train)
from sklearn.metrics import accuracy_score
train_acc = accuracy_score(y_train, train_predictions)

print("The accuracy with the training dataset of the decision tree is: " + str(train_acc))

input("\nPress Enter to continue.\n")



#Prints another application of Decision Trees and considerations
print("\nBelow is another application of decision trees and considerations for using them:\n")
print("Decision trees can be used in areas like loan approval, where banks determine whether to approve a customer based on factors like income, credit score, and employment history. They are popular because the model's decision-making process is easy to interpret and explain to stakeholders. However, decision trees can be prone to overfitting, especially when the tree becomes too deep or complex. Techniques like pruning or using ensemble methods (e.g., Random Forests) can help reduce this risk.")


#Prints a text representation of the Decision Tree
print("\nBelow is a text representation of how the Decision Tree makes choices:\n")
input("\nPress Enter to continue.\n")

util.printTree(clf, X.columns)