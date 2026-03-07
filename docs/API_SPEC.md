# QWX API Specification v1.0

## Endpoints

### POST /v1/ingest
Submit a frame for processing.
- **Payload**: `DetectionSchema`
- **Response**: `202 Accepted` (Task ID)

### GET /v1/results/:task_id
Retrieve recognition results.
- **Response**: `JSON` with plate data and confidence.
