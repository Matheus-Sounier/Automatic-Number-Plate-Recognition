from datetime import datetime
from ultralytics import YOLO

from src.db.data_base import init_db
from src.utils.pipeline import process_frame
from src.utils.persistence import persist_interval, persist_disappeared

import cv2
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

cap = cv2.VideoCapture("./Resources/carLicence4.mp4")
model = YOLO("models/best.pt")
count = 0

init_db()

startTime = datetime.now()
saved_plates = set()
license_plates = {}

cap.release()
cv2.destroyAllWindows()