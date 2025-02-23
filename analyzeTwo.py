import pandas as pd

csv_filename = "data2.csv"
df = pd.read_csv(csv_filename)

x=df["Landmark"]
y=df["Y"]

filtered_values = df[(df['Landmark'] >= 5) & (df['Landmark'] <= 8)]
filtered_values2 = df[(df['Landmark'] >= 9) & (df['Landmark'] <= 12)]

data = filtered_values['Y'].reset_index(drop=True)
data2 = filtered_values2['Y'].reset_index(drop=True)

for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        if(i%4==0):
            print(False)
    if data2[i] < data2[i + 1]:
        if(i%4==0):
            print(False)
    else:
        print("Number of Fingers: 2")