import json
import os

from datetime import datetime

def save_json(license_plates, startTime, endTime):
    interval_data = {
        "Start Time": startTime.isoformat(),
        "End Time": endTime.isoformat(),
        "License Plates": [
            {"plate": plate, "valid": is_valid}
            for plate, is_valid, image in license_plates
        ]
    }