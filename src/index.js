const express = require('express');
const { Queue } = require('bullmq');
const Redis = require('ioredis');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

const connection = new Redis(process.env.REDIS_URL || 'redis://localhost:6379', {
    maxRetriesPerRequest: null
});

const ocrQueue = new Queue('qwx-recognition-tasks', { 
    connection,
    defaultJobOptions: {
        attempts: 3,
        backoff: {
            type: 'exponential',
            delay: 1000,
        },
        removeOnComplete: true
    }
});

app.use(express.json());

app.get('/health', (req, res) => {
    res.status(200).json({
        status: 'healthy',
        service: 'qwx-core-api',
        architecture: 'arm64',
        uptime: process.uptime()
    });
});

app.post('/api/v1/enqueue', async (req, res) => {
    const { document_url, document_type, priority, metadata } = req.body;
    
    if (!document_url) {
        return res.status(400).json({ 
            error: 'Invalid request', 
            message: 'document_url is a required field' 
        });
    }

    try {
        const job = await ocrQueue.add('process_document', {
            url: document_url,
            type: document_type || 'generic_transport_cmr',
            metadata: metadata || {},
            enqueued_at: new Date().toISOString()
        }, { 
            priority: priority || 10 
        });

        return res.status(202).json({ 
            status: 'accepted', 
            jobId: job.id,
            engine_target: 'PaddleOCR/ARM64_Worker' 
        });
    } catch (err) {
        console.error('Failed to enqueue job:', err);
        return res.status(500).json({ error: 'Internal Queue Error' });
    }
});

app.listen(port, () => {
    console.log(`[QWX-CORE] System operational on port ${port} (Architecture: ARM64)`);
});
