
from pathlib import Path
import cv2
from ultralytics import YOLO

# 1. Define project paths
BASE_DIR = Path(__file__).parent
VIDEO_PATH = BASE_DIR / "input_videos" / "newyork.mp4"
OUTPUT_PATH = BASE_DIR / "output_videos" / "detected_video.mp4"

# 2. Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# 3. Open the input video
cap = cv2.VideoCapture(str(VIDEO_PATH))

if not cap.isOpened():
    raise RuntimeError(f"Could not open video: {VIDEO_PATH}")

# 4. Read video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0 or width <= 0 or height <= 0:
    cap.release()
    raise RuntimeError("Invalid video properties.")

# 5. Prepare output video writer
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    str(OUTPUT_PATH),
    fourcc,
    fps,
    (width, height)
)

if not writer.isOpened():
    cap.release()
    raise RuntimeError(f"Could not create output video: {OUTPUT_PATH}")

print("Starting video object detection...")

# 6. Process video frame by frame
try:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Run YOLO object detection
        results = model(frame, verbose=False)

        # Draw bounding boxes and labels
        annotated_frame = results[0].plot()

        # Save processed frame
        writer.write(annotated_frame)

        # Display processed frame
        cv2.imshow("YOLO Video Object Detection", annotated_frame)

        # Press Q to stop early
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Detection stopped by user.")
            break

finally:
    cap.release()
    writer.release()
    cv2.destroyAllWindows()

print(f"Processed video saved to: {OUTPUT_PATH}")
