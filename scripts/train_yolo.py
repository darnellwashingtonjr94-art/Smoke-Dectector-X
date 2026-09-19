from ultralytics import YOLO
import os
import argparse

def train_model(epochs, batch_size, device):
    print("Initializing YOLOv8 training for Smoke-Detector-X...")
    
    # Load pre-trained nano model for edge optimization
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')
    dataset_yaml = os.path.abspath("../data/fire_dataset/data.yaml")
    
    results = model.train(
        data=dataset_yaml,
        epochs=epochs,
        imgsz=640,
        batch=batch_size,
        name='smoke_detector_x_fire',
        device=device
    )
    print(f"Training complete. Weights saved to runs/detect/smoke_detector_x_fire/weights/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train YOLOv8 Fire Detection Model")
    parser.add_argument("--epochs", type=int, default=100, help="Number of training epochs")
    parser.add_argument("--batch", type=int, default=16, help="Batch size")
    parser.add_argument("--device", type=str, default="cpu", help="Device (e.g., 'cpu', 'cuda:0', 'mps')")
    args = parser.parse_args()
    
    train_model(args.epochs, args.batch, args.device)
