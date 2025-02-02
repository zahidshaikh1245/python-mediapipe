import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the hand landmarks CSV data
csv_filename = "hand_landmarks3.csv"
df = pd.read_csv(csv_filename)

# Convert 'Frame' column to integer for sorting
df["Frame"] = df["Frame"].astype(int)

# Assign unique colors to landmarks 5,6,7,8
landmark_palette = {
    0: "black",
    1: "black",
    2: "black",
    3: "black",
    4: "black",
    5: "red",
    6: "blue",
    7: "green",
    8: "purple",
    9: "pink",
    10: "pink",
    11: "pink",
    12: "pink",
    13: "yellow",
    14: "yellow",
    15: "yellow",
    16: "yellow",
    17: "black",
    18: "black",
    19: "black",
    20: "black",
   
}

hand_palette = {0: "orange", 1: "cyan"}  # Assigning colors to hands

# Plot X and Y positions of landmarks for each hand
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="X", y="Y", hue="Landmark", style="Hand", alpha=0.6, palette=landmark_palette)
plt.gca().invert_yaxis()
plt.title("Hand Landmark Positions")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend(title="Landmark")
plt.show()

# Line plot for hand movement over frames
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Frame", y="X", hue="Landmark", marker="o", palette=landmark_palette)
plt.title("X Coordinate Over Time")
plt.xlabel("Frame Number")
plt.ylabel("X Coordinate")
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Frame", y="Y", hue="Landmark", marker="o", palette=landmark_palette)
plt.title("Y Coordinate Over Time")
plt.xlabel("Frame Number")
plt.ylabel("Y Coordinate")
plt.show()