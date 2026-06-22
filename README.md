# FaceNet Facial Recognition Security System

## CST 544 – Artificial Intelligence in Computer Vision

### Week 6 Assignment
### Facial Recognition System for Security Using FaceNet

**Student:** Brent Oatis  
**University:** Concordia University, St. Paul  
**Course:** CST 544 – Artificial Intelligence in Computer Vision  
**Instructor:** Dr. Jeremiah Palmer  
**Date:** June 2026

---

# Project Overview

This project implements a biometric facial recognition security system using FaceNet, MTCNN, OpenCV, and Python.

The system simulates access control at a classified military installation where authorized personnel are verified through facial recognition before being granted access.

FaceNet generates facial embeddings for known personnel and compares them against a test image using Euclidean distance. Access is granted when the similarity score falls within a defined threshold.

---

# Project Objectives

- Detect human faces using MTCNN.
- Generate facial embeddings using FaceNet.
- Compare facial embeddings using Euclidean distance.
- Determine authorized versus unauthorized access.
- Demonstrate practical facial recognition implementation.

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| OpenCV | Image Processing |
| FaceNet | Facial Recognition |
| MTCNN | Face Detection |
| NumPy | Numerical Operations |
| SciPy | Distance Calculations |
| Matplotlib | Visualization |

---

# System Workflow

1. Load authorized personnel images.
2. Detect faces using MTCNN.
3. Extract facial embeddings using FaceNet.
4. Store embeddings in the authorized database.
5. Load test image.
6. Extract test image embedding.
7. Compare embeddings using Euclidean distance.
8. Determine authorization status.

---

# Folder Structure

```text
CST544_Week6_FaceNet_Security_System/
│
├── authorized/
│   ├── brent.jpeg
│   ├── brent_front.jpeg
│   └── brent_smile.jpeg
│
├── test/
│   └── test.jpg
│
├── outputs/
│   ├── authorized_output.png
│   └── not_authorized_output.png
│
├── facenet_security.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Execute the script:

```bash
python facenet_security.py
```

The system will:

- Build the authorized personnel database.
- Generate FaceNet embeddings.
- Compare the test image.
- Return an authorization decision.

---

# Sample Results

## Authorized User

| Metric | Value |
|----------|----------|
| Identity | Brent Oatis |
| Distance Score | 0.5773 |
| Threshold | 0.9 |
| Result | Authorized |

Result:

```text
Access Granted
```

---

## Unauthorized User

| Metric | Value |
|----------|----------|
| Identity | Unknown Individual |
| Distance Score | 1.5081 |
| Threshold | 0.9 |
| Result | Unauthorized |

Result:

```text
Access Denied
```

---

# Challenges Encountered

- Lighting variation between images.
- Facial pose differences.
- Threshold selection.
- Limited image dataset.
- Face detection reliability.

---

# Lessons Learned

- High-quality reference images improve accuracy.
- FaceNet embeddings are highly effective for recognition.
- Threshold tuning is critical.
- Multiple images per authorized user improve robustness.
- Facial recognition systems require continuous validation.

---

# Future Enhancements

- Real-time webcam authentication.
- Edge AI deployment.
- Liveness detection.
- Deepfake detection.
- Multi-factor authentication.
- Expanded personnel database.

---

# References

Anand, A. (2024). *How to build a face recognition system using FaceNet in Python*. DEV Community. https://dev.to/abhinowww/how-to-build-a-face-recognition-system-using-facenet-in-python-27kh

Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A unified embedding for face recognition and clustering. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 815–823.

Timesler. (n.d.). *FaceNet-PyTorch*. GitHub. https://github.com/timesler/facenet-pytorch

Vishal. (2024). *Face detection and recognition capable of beating humans using FaceNet*. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/06/face-detection-and-recognition-capable-of-beating-humans-using-facenet/

---

# Author

**Brent Oatis**

MBA Candidate – Artificial Intelligence Concentration

Concordia University, St. Paul

CST 544 – Artificial Intelligence in Computer Vision

June 2026