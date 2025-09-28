# Application settings
import os

# YOLO Model Settings
YOLO_MODEL_PATH = "models/best.pt" # Path to your trained YOLO model weights
YOLO_CONFIDENCE_THRESHOLD = 0.5 # Minimum confidence to consider a detection

# GPS Settings
DEFAULT_SEARCH_RADIUS_KM = 5 # Default radius for searching nearby hospitals

# Other settings
LOG_FILE_PATH = "app_log.log"