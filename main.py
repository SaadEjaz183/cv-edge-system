import argparse
import cv2
from ultralytics import YOLO
from utils.draw import draw_detections
from utils.fps import FPSCounter

def main():
    parser = argparse.ArgumentParser(description="Real-time object detection")
    parser.add_argument("--source", type=int, default=0, help="Camera index (default 0)")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="YOLO model weights")
    parser.add_argument("--conf", type=float, default=0.4, help="Confidence threshold")
    parser.add_argument("--classes", type=int, nargs="+", default=None, help="Filter specific class IDs")
    args = parser.parse_args()

    print("Loading model...")
    model = YOLO(args.model)

    cap = cv2.VideoCapture(args.source)
    if not cap.isOpened():
        print(f"Error: Could not open camera source {args.source}")
        return

    fps_counter = FPSCounter()
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        results = model.predict(frame, conf=args.conf, classes=args.classes, verbose=False)
        frame = draw_detections(frame, results[0])

        fps = fps_counter.update()
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Real-Time Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()