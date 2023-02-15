import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QFileDialog
import os

# Create a Qt application
app = QApplication([])

# Prompt the user to select a file
file_dialog = QFileDialog()
file_dialog.setNameFilter("CSV files (*.csv)")
file_dialog.exec()

# Get the selected file path
file_paths = file_dialog.selectedFiles()
if file_paths:
    file_path = file_paths[0]
    file_name = os.path.basename(file_path)
else:
    file_name = ""

# Read in the CSV data using pandas
data = pd.read_csv(file_path)

# Extract the column names and data from the DataFrame
column_names = list(data.columns)

# Plot each column in a separate subplot
num_columns = len(column_names)
fig, axs = plt.subplots(num_columns, 1, figsize=(8, num_columns*3), sharex=True)
fig.suptitle(f'{file_name}', fontsize=20, fontweight='bold')
fig.subplots_adjust(top=0.9)
for i in range(num_columns):
    column_name = column_names[i]
    x_data = data[column_name]
    axs[i].plot(x_data)
    axs[i].set_ylabel(column_name)

# Display the chart
plt.show()

# Exit the Qt application
app.exit()
