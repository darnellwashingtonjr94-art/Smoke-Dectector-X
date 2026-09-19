from ultralytics import YOLO

class FireDetector:
    def __init__(self, model_path, confidence_threshold=0.65):
        self.model = YOLO(model_path)
        self.threshold = confidence_threshold

    def detect(self, frame):
        """
        Runs YOLOv8 inference on the provided frame.
        Expects 'fire' to be class 0 in the trained weights.
        """
        results = self.model(frame, verbose=False)
        
        for result in results:
            boxes = result.boxes
            for box in boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                
                if cls == 0 and conf >= self.threshold:
                    return True, conf, box.xyxy[0].tolist()
                    
        return False, 0.0, []
