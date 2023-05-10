import sys
import time

import psutil
from ultralytics import YOLO


def get_ram_usage():
    return psutil.virtual_memory().used / (1024 ** 2)


def export_and_measure_ram(export_format, model_path, output_file):
    model = YOLO(model_path)

    for _ in range(30):
        model.export(format=export_format)
        ram_usage = get_ram_usage()

        with open(output_file, 'a') as f:
            f.write(f'{export_format},{ram_usage}\n')

        time.sleep(1)  # Allow time for garbage collection between exports


export_format = sys.argv[1]
model_path = 'yolov8n.pt'
output_file = sys.argv[2]

export_and_measure_ram(export_format, model_path, output_file)
