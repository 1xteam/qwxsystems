# QWX System (Open-Source Core)

High-performance distributed computer vision platform for real-time vehicle identification, Automatic License Plate Recognition (ALPR), and logistics document digitization optimized for ARM64 environments (AWS Graviton3).

QWX bridges physical vehicle flow with digital logistics systems by combining object detection, tracking, OCR, and rule-based normalization in a distributed pipeline.

---

## Core Capabilities

- Real-time Automatic License Plate Recognition (ALPR)
- Vehicle tracking using multi-object tracking
- Document digitization for CMR, waybills, and logistics forms
- Distributed inference pipeline
- High-throughput asynchronous processing
- ARM64 optimized runtime for cost-efficient cloud deployment

---

## System Architecture

QWX uses a distributed micro-pipeline architecture separating API orchestration from compute-heavy computer vision inference.

Camera / Stream  
↓  
Frame Ingestion (Node.js API Gateway)  
↓  
Redis Task Queue (BullMQ)  
↓  
Python Processing Workers  
• Object Detection (YOLOv8 / YOLOv10)  
• Multi-Object Tracking (DeepSORT)  
• OCR Extraction (PaddleOCR / Tesseract)  
↓  
Post-Processing Engine  
• Plate normalization  
• Confidence scoring  
• Format validation  
↓  
Structured Output (JSON / ERP Integration)

---

## Distributed Processing Model

Node API  
↓ enqueue  
Redis Queue  
↓ distribute tasks  
Worker Pool (Python)  
• detection  
• OCR  
• normalization  

Advantages:

- Non-blocking API layer
- Horizontal worker scaling
- Isolation of CPU-bound CV workloads
- Fault-tolerant distributed pipeline

---

## Technology Stack

### Runtime
- Node.js 20+
- Python 3.11+

### Computer Vision
- OpenCV
- YOLOv8 / YOLOv10
- DeepSORT

### OCR
- PaddleOCR
- Tesseract
- LayoutParser

### Data Infrastructure
- PostgreSQL
- Redis
- BullMQ

### Infrastructure
- Docker
- Docker Compose
- AWS SDK
- GitHub Actions

---

## ARM64 Optimization

QWX is designed to run efficiently on ARM64 cloud infrastructure, especially:

AWS Graviton3 (r7g / t4g instances)

Benefits:

- lower compute cost
- improved performance per watt
- efficient large-scale inference clusters

---

## Example Processing Flow

Input Frame  
↓  
Vehicle Detection  
↓  
License Plate Detection  
↓  
Plate Crop  
↓  
OCR Extraction  
↓  
Normalization  
↓  
Structured Output

Example output:

{
  "vehicle_id": "frame_1721",
  "plate": "80A123BC",
  "confidence": 0.97,
  "timestamp": "2026-03-07T11:20:31Z"
}

---

## Repository Structure

qwxsystems  
├ src/ (Node.js API gateway)  
├ workers/ (Python CV processing nodes)  
├ tests/ (unit and integration tests)  
├ docker-compose.yml  
├ requirements.txt  
├ package.json  
└ README.md  

---

## Quick Start (Development)

In development...

## Example API Health Check

GET /health

Response

{
  "status": "ok",
  "service": "qwx-api"
}

---

## Use Cases

### Smart Parking and Access Control

Automated vehicle entry and exit validation with dwell-time analytics.

### Secure Facility Monitoring

Vehicle tracking and unauthorized access detection in restricted zones.

### Logistics Checkpoints

Automated truck identification and transport document digitization.

---

## Roadmap

- GPU acceleration support
- ONNX runtime optimization
- Kafka ingestion pipeline
- Multi-camera synchronization
- Edge deployment support
- Advanced plate normalization

---

## Demo

Input frame → detected license plate → OCR result

Example:

Plate: 45A123BC  
Confidence: 0.97

## License

MIT License

Open-source core of the QWX distributed computer vision platform.
