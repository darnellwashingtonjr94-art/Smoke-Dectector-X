from ultralytics import YOLO

def export_model():
    """
    Exports the trained PyTorch (.pt) model to TensorRT (.engine).
    This is highly recommended for Jetson Nano deployments to achieve real-time FPS.
    """
    model_path = "../models/yolov8_fire_custom.pt"
    print(f"Loading PyTorch model from {model_path}...")
    
    model = YOLO(model_path)
    
    print("Exporting to TensorRT...")
    # Requires TensorRT to be installed on the deployment device
    model.export(format="engine", half=True) # half=True uses FP16 precision
    
    print("Export complete! .engine file generated for high-speed edge inference.")

if __name__ == "__main__":
    export_model()
