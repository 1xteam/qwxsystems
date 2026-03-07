const Joi = require('joi');

const detectionSchema = Joi.object({
    stream_id: Joi.string().uuid().required(),
    timestamp: Joi.date().iso().required(),
    frame_data: Joi.string().base64().required(), // Base64 image
    metadata: Joi.object({
        location_id: Joi.string(),
        camera_type: Joi.string().valid('ptz', 'fixed')
    })
});

module.exports = { detectionSchema };
