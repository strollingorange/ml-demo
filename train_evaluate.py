from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

# Load Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% testing

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Initialize KNN classifier
classifier = KNeighborsClassifier(n_neighbors=5)

# Train the model using the training sets
classifier.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = classifier.predict(X_test)

# Evaluating the Model
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the confusion matrix to a CSV file
pd.DataFrame(cm, index=iris.target_names, columns=iris.target_names).to_csv('confusion_matrix.csv', index=True)

print("Confusion matrix saved to 'confusion_matrix.csv'")
