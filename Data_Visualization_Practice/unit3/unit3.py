import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/nimba/OneDrive/Desktop/Data_Visualization_Practice/unit3/tips.csv")

# Style
sns.set(style="whitegrid")

# -----------------------------
# 1. Scatter Plot (Better using seaborn)
# -----------------------------
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# -----------------------------
# 2. Line Chart (Sorted for proper trend)
# -----------------------------
df_sorted = df.sort_values(by='total_bill')

plt.figure()
plt.plot(df_sorted['total_bill'], df_sorted['tip'], marker='o')
plt.title("Line Chart: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# -----------------------------
# 3. Bar Chart (Cleaner using seaborn)
# -----------------------------
plt.figure()
sns.barplot(x='sex', y='tip', data=df)
plt.title("Bar Chart: Average Tip by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip")
plt.show()

# -----------------------------
# 4. Histogram (Better visualization)
# -----------------------------
plt.figure()
sns.histplot(df['total_bill'], bins=5, kde=True)
plt.title("Histogram: Total Bill Distribution")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()