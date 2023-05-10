import csv
import os
from collections import defaultdict

import matplotlib.pyplot as plt

csv_filename = 'ram_usage_data.csv'

# Remove the CSV file if it exists
if os.path.exists(csv_filename):
    os.remove(csv_filename)

# export_formats = ["torchscript", "onnx", "openvino", "engine", "coreml", "saved_model", "pb", "tflite", "edgetpu", "tfjs", "paddle"]
export_formats = [
    'torchscript', 'onnx', 'openvino', 'coreml', 'saved_model', 'pb', 'tflite', 'edgetpu', 'tfjs', 'paddle']

# Run measure_ram_usage.py for each export format
for export_format in export_formats:
    os.system(f'python3 measure_ram_usage.py {export_format} {csv_filename}')

# Read the CSV file and store the data
ram_usage_data = defaultdict(list)
with open(csv_filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        export_format, ram_usage = row
        ram_usage_data[export_format].append(float(ram_usage))

# Plot the results
fig, ax = plt.subplots()

for export_format, ram_usages in ram_usage_data.items():
    x_values = list(range(1, len(ram_usages) + 1))
    ax.plot(x_values, ram_usages, label=export_format, marker='o')

ax.set_xlabel('Exports')
ax.set_ylabel('System RAM usage (MB)')
ax.legend(loc='best')
plt.tight_layout()
plt.show()
plt.savefig('ram_usage_plot.png', dpi=300, bbox_inches='tight')
