import pandas as pd

# Read the CSV file
df = pd.read_csv('test.csv')

# List of landmarks you want the y coordinates for
landmarks_to_extract = [5, 6, 7, 8]

# Filter the DataFrame for the selected landmarks and extract the 'y' coordinates
y_coordinates = df[df['landmark'].isin(landmarks_to_extract)]['y'].tolist()  # Convert to list

# Print the y coordinates as an array
print("Y-coordinates as an array:", y_coordinates)
