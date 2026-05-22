import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("data.csv")

print("\nOriginal Dataset Shape:")
print(df.shape)

# -----------------------------
# DATA CLEANING
# -----------------------------
df = df.dropna()

df = df.drop_duplicates()

print("\nCleaned Dataset Shape:")
print(df.shape)

# -----------------------------
# DATA SUMMARY
# -----------------------------
summary = df.describe()

print("\nDataset Summary:\n")

print(summary)

# -----------------------------
# EXPORT CLEANED DATA
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Dataset Exported!")

# -----------------------------
# GENERATE REPORT
# -----------------------------
report = open("report.txt", "w")

report.write("DATA CLEANING REPORT\n\n")

report.write(str(summary))

report.close()

print("\nReport Generated Successfully!")

# -----------------------------
# BAR CHART
# -----------------------------
plt.bar(df.index[:10], df['G3'][:10])

plt.xlabel("Students")

plt.ylabel("Final Grade")

plt.title("Student Final Grades")

plt.savefig("bar_chart.png")

plt.show()

# -----------------------------
# PIE CHART
# -----------------------------
df['failures'].value_counts().plot.pie(
    autopct='%1.1f%%'
)

plt.title("Failure Distribution")

plt.ylabel("")

plt.savefig("pie_chart.png")

plt.show()