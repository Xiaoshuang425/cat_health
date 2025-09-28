# YOLO model loading and inference
from ultralytics import YOLO
import cv2
import numpy as np

class CatPoopDetector:
    def __init__(self, model_path="models/best.pt"):
        """
        Initializes the YOLO model for cat poop detection.
        Args:
            model_path (str): Path to the trained YOLO model weights.
        """
        self.model = YOLO(model_path)
        self.class_names = self.model.names # Get class names from the model

    def detect(self, image_path):
        """
        Performs inference on an image to detect cat poop characteristics.
        Args:
            image_path (str): Path to the input image.
        Returns:
            list: A list of detected objects, each containing bounding box, confidence, and class.
        """
        results = self.model(image_path)
        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = round(float(box.conf[0]), 2)
                class_id = int(box.cls[0])
                class_name = self.class_names[class_id]
                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "confidence": confidence,
                    "class_name": class_name
                })
        return detections

    def draw_boxes(self, image_path, detections, output_path="output.jpg"):
        """
        Draws bounding boxes and labels on the image.
        Args:
            image_path (str): Path to the input image.
            detections (list): List of detected objects.
            output_path (str): Path to save the output image.
        """
        img = cv2.imread(image_path)
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            class_name = det["class_name"]
            confidence = det["confidence"]
            color = (0, 255, 0)  # Green color for bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, f"{class_name} {confidence}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.imwrite(output_path, img)
        print(f"Detection image saved to {output_path}")

if __name__ == "__main__":
    # Example usage (requires a trained model and an image)
    # detector = CatPoopDetector(model_path="../../models/best.pt") # Adjust path as needed
    # detections = detector.detect("../../data/sample_poop.jpg") # Adjust path as needed
    # print("Detections:", detections)
    # detector.draw_boxes("../../data/sample_poop.jpg", detections)
    pass