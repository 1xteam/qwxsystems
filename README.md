# QWX System (Open-Source Core)

**High-Performance Computer Vision & Logistics Intelligence Suite optimized for ARM64.**

## Overview
QWX System is an enterprise-grade distributed platform designed for real-time vehicle identification, automated license plate recognition (ALPR), and logistics document digitization. 

The core engine is architected for **ARM64 (AWS Graviton3)** environments, delivering high-throughput processing for smart parking, secure access control, and automated supply chain checkpoints. By combining real-time Object Detection with structural OCR, QWX bridges the gap between physical vehicle flow and digital ERP systems.

## Key Use Cases
* **Smart Parking & Access Control:** Automated vehicle entry/exit validation using ALPR and dwell-time analytics.
* **High-Security Monitoring:** Real-time multi-object tracking (MOT) and unauthorized vehicle detection in restricted zones.
* **Logistics Automation:** Simultaneous recognition of vehicle identifiers and digital processing of transport documents (CMR, Waybills).

## Architecture
* **QWX-API:** High-concurrency Node.js gateway for stream ingestion and state management.
* **QWX-Worker:** Python-based processing nodes utilizing neural networks for object detection (YOLO) and document segmentation.
* **QWX-Intelligence:** Dynamic rule engine for mapping unstructured CV data into standardized JSON schemas.
* **Infrastructure:** Optimized for **AWS Graviton3 (r7g/t4g)** with Redis-backed task queuing via BullMQ.

## Features
* **Hybrid Recognition Engine:** Integrated support for YOLOv8/v10 (Detection), DeepSORT (Tracking), and PaddleOCR (Text Extraction).
* **ARM64 Native Performance:** Up to 25% efficiency increase on Graviton3 vs x86_64, reducing operational costs for large-scale deployments.
* **Asynchronous Processing:** Distributed worker architecture for parallelizing heavy CV tasks.
* **Audit Trail:** Full versioning and verification of extracted identifiers and telemetry.

## Tech Stack
* **Runtimes:** Node.js 20+, Python 3.11+
* **Computer Vision:** OpenCV, YOLOv8/v10, DeepSORT.
* **OCR Layer:** PaddleOCR, Tesseract, LayoutParser.
* **Data Store:** PostgreSQL, Redis (IO/Cache).
* **Ops:** Docker & Docker Compose, AWS SDK, GitHub Actions.

## Installation (Development) License
```bash
In the process of development, waiting...



