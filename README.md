# Video Object Detection Using YOLO

A computer vision project that detects objects in video footage using YOLO, Python, and OpenCV.

## Project Overview

This project processes a video frame by frame and identifies objects using a pretrained YOLO model. It draws bounding boxes around detected objects and saves the processed video as an output file.

## Features

- Video processing using OpenCV
- Object detection using YOLO11n
- Detection of common objects, including people, cars, trucks, and buses
- Adjustable confidence threshold
- Customizable bounding box thickness
- Export of the processed video to MP4

## Technologies Used

- Python
- Ultralytics YOLO11
- OpenCV
- PyTorch

## Project Structure

```text
Video-Object-Detection/
├── main.py
├── .gitignore
├── README.md
├── input_videos/
└── output_videos/
```

The input and output video folders are used locally and are excluded from GitHub uploads.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/wahidali4321/Video-Object-Detection.git
cd Video-Object-Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install ultralytics opencv-python
```

PyTorch is used by Ultralytics and may be installed automatically as a dependency. For GPU acceleration, install a PyTorch version compatible with your CUDA environment.

## How to Run

1. Place your input video inside the `input_videos` folder.
2. Ensure the video path in `main.py` matches your input file.
3. Run the script:

```bash
python main.py
```

4. Find the processed video in the `output_videos` folder.

## Model

This project uses the pretrained YOLO11n model, a lightweight object detection model suitable for experimenting with computer vision applications.

## Learning Outcomes

- Understanding object detection workflows
- Processing video frames with OpenCV
- Running YOLO inference on video
- Visualizing model predictions
- Saving processed video output

## Future Improvements

- Improve detection accuracy and inference speed
- Add object tracking across video frames
- Display detection counts for each object class
- Build a web interface for uploading and processing videos

## Author

**Wahid Ali**

Aspiring Computer Vision Engineer

GitHub: [wahidali4321](https://github.com/wahidali4321)

---

If you find this project useful, feel free to explore the repository and share feedback.
