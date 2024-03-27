import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

chunk_size = 50000  # This is the number of lines
chunks = []

# Specify the format for the datetime conversion
date_format = '%d/%m/%Y%H:%M:%S'

for chunk in pd.read_csv('data.csv', chunksize=chunk_size):
    # Convert 'Timestamp' column to datetime with the specified format
    chunk['Timestamp'] = pd.to_datetime(chunk['Timestamp'], format=date_format)
    # Set 'Timestamp' as the index
    chunk.set_index('Timestamp', inplace=True)
    chunks.append(chunk['Total.Fwd.Packets'])

# Concatenate the list into a single DataFrame
time_series = pd.concat(chunks)
#test
# Plotting
time_series.plot(figsize=(10, 6))  # Adjust the figure size as needed
plt.title('Total Forward Packets Over Time')  # Add a title
plt.xlabel('Timestamp')  # Label for the x-axis
plt.ylabel('Total Forward Packets')  # Label for the y-axis
plt.show()
