# CreateNow API Documentation

## Generation Endpoint

The generation endpoint allows you to create AI-generated content (images, music, videos, or speech) using natural language prompts.

### Endpoint
```
POST https://createnow.xyz/api/v1/generate
```

### Authentication
All requests require a Bearer token in the Authorization header:
```
Authorization: Bearer YOUR_API_KEY
```

### Basic Usage

The simplest way to use the API is to just send a prompt. Our system will automatically detect the most appropriate media type based on your prompt.
```json
{
"prompt": "a beautiful sunset over the ocean"
}
```


### Advanced Options

You can explicitly specify options:
```json
{
"prompt": "your prompt here",
"type": "image" | "music" | "video" | "speech", // optional: specify media type
"count": 1-4, // optional: number of outputs (default: 1)
"duration": 30 // optional: for music/speech (in seconds)
}
```


### Response Format

Success Response:
```json
{
"success": true,
"outputs": [
{
"url": "storage-link-here",
"creation_id": "id-here",
"share_url": "https://createnow.xyz/share/{id-here}"
}
],
"mediaType": "image", // Detected or specified media type
"confidence": 0.95, // Confidence score for auto-detection
"detected": true // Whether media type was auto-detected
}
```


Error Response:
```json
{
"error": "error message here",
"status": 400 | 401 | 402 | 500
}
```

### Examples

1. Auto-detected Image Generation:
```json
{
"prompt": "create a watercolor painting of a cat"
}
```


2. Explicit Music Generation with Duration:
```json
{
"prompt": "create an upbeat jazz melody",
"type": "music",
"duration": 30
}
```

3. Multiple Image Generation:
```json
{
"prompt": "generate product photos of a modern chair",
"type": "image",
"count": 4
}
```

### Error Codes
- `400`: Bad Request (invalid parameters)
- `401`: Unauthorized (invalid API key)
- `402`: Payment Required (insufficient credits)
- `500`: Server Error

### Notes
- Maximum prompt length: 1000 characters
- Maximum generation count: 4 outputs per request
- Supported media types: image, music, video, speech
- Auto-detection uses natural language processing to determine the most appropriate media type
- Each output includes a unique creation ID and shareable URL
