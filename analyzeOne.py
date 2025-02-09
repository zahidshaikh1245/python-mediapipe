import pandas as pd

csv_filename = "data.csv"
df = pd.read_csv(csv_filename)

x=df["Landmark"]
y=df["Y"]

filtered_values = df[(df['Landmark'] >= 5) & (df['Landmark'] <= 8)]

data = filtered_values['Y'].reset_index(drop=True)

for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        if(i%4==0):
            print(False)
    else:
        print(True)
