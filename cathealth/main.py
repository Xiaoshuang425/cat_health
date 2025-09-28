# Main application entry point
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    print("YOLO Cat Health Detection Application")
    # Here you would integrate the different modules:
    # 1. Image capture/upload
    # 2. YOLO inference (src/yolo/model.py)
    # 3. Health analysis (src/health_analyzer/analyzer.py)
    # 4. GPS location and hospital search (src/gps/locator.py)
    # 5. Display results and recommendations

    # Example: Accessing a setting from config/settings.py
    # from config.settings import YOLO_MODEL_PATH
    # print(f"YOLO Model Path: {YOLO_MODEL_PATH}")

    # Example: Accessing an environment variable
    # api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    # if api_key:
    #     print("Google Maps API Key loaded.")
    # else:
    #     print("Google Maps API Key not found. Please set it in a .env file.")

if __name__ == "__main__":
    main()