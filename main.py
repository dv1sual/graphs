import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QFileDialog

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

# Read in the CSV data using pandas
data = pd.read_csv(file_path)

# Extract the data for each column
x_data = data['Head 0 FPS']
#  y_data = data['Head 1 FPS'] #  might be useful for 4 out servers
#  z_data = data['Head 2 FPS']
#  w_data = data['Head 3 FPS']

# Create a line chart using matplotlib
plt.plot(x_data)

# Add grid lines to the chart
plt.grid(True)

# Create a line chart using matplotlib
plt.plot(x_data, color='red', linestyle='-')


# Set the title and axis labels
plt.title("FPS Monitor")
plt.xlabel("Head 0")
plt.ylabel("FPS")

# Display the chart
plt.show()

# Exit the Qt application
app.exit()
