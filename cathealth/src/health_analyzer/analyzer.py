# Health risk analysis logic
class HealthAnalyzer:
    def __init__(self):
        # Define health risk rules based on poop characteristics
        self.risk_rules = {
            "color": {
                "black": {"severity": "high", "message": "可能存在消化道出血，請立即就醫。"},
                "red": {"severity": "high", "message": "可能存在下消化道出血或寄生蟲，請立即就醫。"},
                "yellow": {"severity": "medium", "message": "可能存在肝膽問題或消化不良，請觀察。"},
                "green": {"severity": "medium", "message": "可能攝入過多綠色食物或膽汁分泌異常，請觀察。"},
                "brown": {"severity": "low", "message": "正常。"}
            },
            "texture": {
                "liquid": {"severity": "high", "message": "嚴重腹瀉，可能脫水，請立即就醫。"},
                "soft": {"severity": "medium", "message": "輕微腹瀉或飲食不適，請觀察。"},
                "firm": {"severity": "low", "message": "正常。"},
                "hard": {"severity": "medium", "message": "便秘，可能飲水不足或纖維攝入不足，請觀察。"}
            },
            "shape": {
                "pellets": {"severity": "medium", "message": "便秘，可能飲水不足或纖維攝入不足，請觀察。"},
                "log": {"severity": "low", "message": "正常。"},
                "pudding": {"severity": "medium", "message": "輕微腹瀉或飲食不適，請觀察。"},
                "watery": {"severity": "high", "message": "嚴重腹瀉，可能脫水，請立即就醫。"}
            }
        }

    def analyze(self, detections):
        """
        Analyzes detected cat poop characteristics to assess health risk.
        Args:
            detections (list): A list of detected objects from the YOLO model.
        Returns:
            dict: A dictionary containing overall health status, severity, and recommendations.
        """
        overall_severity = "low"
        recommendations = []
        detected_characteristics = {}

        for det in detections:
            class_name = det["class_name"]
            # Assuming class names are like "color_brown", "texture_firm", "shape_log"
            if "_" in class_name:
                category, value = class_name.split("_", 1)
                detected_characteristics[category] = value

        for category, value in detected_characteristics.items():
            if category in self.risk_rules and value in self.risk_rules[category]:
                rule = self.risk_rules[category][value]
                recommendations.append(f"{category.capitalize()}: {value} - {rule['message']}")
                if self._get_severity_level(rule['severity']) > self._get_severity_level(overall_severity):
                    overall_severity = rule['severity']

        if not recommendations:
            recommendations.append("未檢測到異常，貓咪糞便狀況良好。")
            overall_severity = "low"

        return {
            "overall_status": "異常" if overall_severity != "low" else "正常",
            "severity": overall_severity,
            "recommendations": recommendations
        }

    def _get_severity_level(self, severity_str):
        """Helper to convert severity string to an integer level for comparison."""
        levels = {"low": 0, "medium": 1, "high": 2}
        return levels.get(severity_str, 0)

if __name__ == "__main__":
    analyzer = HealthAnalyzer()
    # Example detections from YOLO model
    sample_detections_normal = [
        {"bbox": [10, 10, 50, 50], "confidence": 0.95, "class_name": "color_brown"},
        {"bbox": [60, 60, 100, 100], "confidence": 0.92, "class_name": "texture_firm"},
        {"bbox": [110, 110, 150, 150], "confidence": 0.90, "class_name": "shape_log"}
    ]
    analysis_normal = analyzer.analyze(sample_detections_normal)
    print("Normal Analysis:", analysis_normal)

    sample_detections_high_risk = [
        {"bbox": [10, 10, 50, 50], "confidence": 0.95, "class_name": "color_black"},
        {"bbox": [60, 60, 100, 100], "confidence": 0.92, "class_name": "texture_liquid"},
        {"bbox": [110, 110, 150, 150], "confidence": 0.90, "class_name": "shape_watery"}
    ]
    analysis_high_risk = analyzer.analyze(sample_detections_high_risk)
    print("High Risk Analysis:", analysis_high_risk)