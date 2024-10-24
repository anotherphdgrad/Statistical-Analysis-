import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mannwhitneyu

# Use this code approach wise Run for Fedavg and HA-FL. 
# Expectations is:
# Fedavg will show statistically significant differences (Reject the null hypothesis)
# HA-FL will NOT show statistically significant differences (Accept the null hypothesis)

# Data for the two groups
women_accuracy = [0.85, 0.87, 0.80, 0.82, 0.83, 0.86, 0.88, 0.81]
men_accuracy = [0.75, 0.77, 0.79, 0.80, 0.74, 0.78, 0.81, 0.76, 0.79, 0.77, 0.78, 0.80]

# Create histograms to show the distribution of accuracies
plt.figure(figsize=(10, 6))

# Plot histograms
plt.hist(women_accuracy, bins=np.arange(0.7, 0.91, 0.02), alpha=0.5, label="Women", color='blue', edgecolor='black') #Shaily--We need to change arange based on the excel sheets
plt.hist(men_accuracy, bins=np.arange(0.7, 0.91, 0.02), alpha=0.5, label="Men", color='green', edgecolor='black') #-We need to change arange based on the excel sheets

# Add labels and title
plt.xlabel("Accuracy")
plt.ylabel("Frequency")
plt.title("Accuracy Distribution for Men and Women")
plt.legend()

# Show the plot
plt.show()

# Perform the Mann-Whitney U test
stat, p_value = mannwhitneyu(women_accuracy, men_accuracy)

# Output the U statistic and p-value
print(f"Mann-Whitney U statistic: {stat}")
print(f"P-value: {p_value}")

# Interpretation of results
if p_value < 0.05:
    print("There is a statistically significant difference between the accuracy distributions for men and women.")
else:
    print("There is no statistically significant difference between the accuracy distributions for men and women.")
