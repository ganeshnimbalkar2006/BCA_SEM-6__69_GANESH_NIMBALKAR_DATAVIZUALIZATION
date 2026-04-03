import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# (a) Random Array Visualization
# -------------------------------
data = np.random.randint(1, 100, 50)

plt.figure(figsize=(12,8))

# Line Chart
plt.subplot(2,2,1)
plt.plot(data)
plt.title("Line Chart")

# Scatter Plot
plt.subplot(2,2,2)
plt.scatter(range(50), data)
plt.title("Scatter Plot")

# Histogram
plt.subplot(2,2,3)
plt.hist(data)
plt.title("Histogram")

# Box Plot
plt.subplot(2,2,4)
plt.boxplot(data)
plt.title("Box Plot")

plt.tight_layout()
plt.show()

# -------------------------------
# (b) Add Outliers
# -------------------------------
data_with_outliers = list(data)
data_with_outliers.extend([200, 250])

plt.boxplot(data_with_outliers)
plt.title("Box Plot with Outliers")
plt.show()

# -------------------------------
# (c) Pie Chart & Bar Chart
# -------------------------------
subjects = ['Math', 'English', 'Science', 'CS', 'History']
marks = [85, 78, 90, 88, 76]

plt.figure(figsize=(10,5))

# Pie Chart
plt.subplot(1,2,1)
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")

# Bar Chart
plt.subplot(1,2,2)
plt.bar(subjects, marks)
plt.title("Marks Bar Chart")

plt.tight_layout()
plt.show()

# -------------------------------
# Load Iris Dataset
# -------------------------------
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# -------------------------------
# (d) Bar Plot - Species Frequency
# -------------------------------
df['species'].value_counts().plot(kind='bar')
plt.title("Species Frequency")
plt.show()

# -------------------------------
# (e) Pie Plot - Species Frequency
# -------------------------------
df['species'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Species Distribution")
plt.show()

# -------------------------------
# (f) Histogram
# -------------------------------
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Iris Features")
plt.show()

# -------------------------------
# (g) Petal Length vs Width
# -------------------------------
plt.scatter(df['petal length (cm)'], df['petal width (cm)'])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Width")
plt.show()

# -------------------------------
# (h) Scatter Plot Comparison
# -------------------------------
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Comparison")
plt.show()

# -------------------------------
# Box Plots for all features
# -------------------------------
features = [
    'sepal length (cm)', 
    'sepal width (cm)', 
    'petal length (cm)', 
    'petal width (cm)'
]

for feature in features:
    sns.boxplot(x='species', y=feature, data=df)
    plt.title(f"{feature} vs Species")
    plt.show()