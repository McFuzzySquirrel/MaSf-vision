# School Edge Node API Documentation

## Overview

The School Edge Node API provides REST endpoints for mobile devices to discover and interact with edge services. This API Gateway enables mobile-to-edge communication for the MaSf-vision platform.

## Base URL

```
http://<edge-node-ip>:8000
```

## Authentication

Currently, no authentication is required. This is suitable for local network deployment. For production deployments, consider adding:
- API key authentication
- JWT tokens
- mTLS for device certificates

## Core Endpoints

### 1. Service Discovery

**Endpoint**: `GET /api/v1/discover`

**Description**: Primary endpoint for mobile devices to discover the edge node and its capabilities.

**Response**:
```json
{
  "node_id": "edge-node-001",
  "node_name": "School Edge Node",
  "version": "1.0.0",
  "status": "operational",
  "capabilities": [
    "api_gateway",
    "service_discovery"
  ],
  "timestamp": "2026-02-16T21:00:00.000000"
}
```

### 2. Health Check

**Endpoint**: `GET /health`

**Description**: Check the operational status of the edge node and its services.

**Response**:
```json
{
  "status": "operational",
  "timestamp": "2026-02-16T21:00:00.000000",
  "services": [
    {
      "service_name": "api_gateway",
      "status": "healthy",
      "available": true
    }
  ]
}
```

### 3. List Services

**Endpoint**: `GET /api/v1/services`

**Description**: Get a list of all available services and their status.

**Response**:
```json
{
  "services": [
    {
      "name": "API Gateway",
      "endpoint": "/api/v1",
      "status": "operational",
      "description": "REST API for mobile device integration"
    }
  ]
}
```

### 4. Node Status

**Endpoint**: `GET /api/v1/status`

**Description**: Get detailed status information about the edge node.

**Response**:
```json
{
  "node_id": "edge-node-001",
  "uptime": "unknown",
  "connected_devices": 0,
  "services_running": 2,
  "services_total": 5,
  "storage_available": "unknown",
  "load_average": "unknown",
  "last_updated": "2026-02-16T21:00:00.000000"
}
```

## Future Endpoints (Not Yet Implemented)

These endpoints are defined but will return HTTP 501 (Not Implemented):

### Content Distribution
- `GET /api/v1/content/packages` - List available content packages
- `GET /api/v1/content/packages/{package_id}` - Download content package

### Model Inference
- `POST /api/v1/inference` - Run ML model inference

### Sync Coordination
- `POST /api/v1/sync/upload` - Upload sync data from mobile devices

## Interactive Documentation

The API includes auto-generated interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Error Responses

### 501 Not Implemented
Returned when accessing endpoints for services not yet implemented:
```json
{
  "detail": "Content distribution service not yet implemented"
}
```

### 404 Not Found
Returned when accessing non-existent endpoints:
```json
{
  "detail": "Not Found"
}
```

## CORS Configuration

The API is configured to accept requests from any origin (`*`) for development. In production:
1. Specify allowed mobile app origins
2. Configure proper CORS policies
3. Enable authentication

## Integration Example

### Python
```python
import requests

# Discover edge node
response = requests.get("http://192.168.1.100:8000/api/v1/discover")
node_info = response.json()
print(f"Connected to: {node_info['node_name']}")
print(f"Capabilities: {node_info['capabilities']}")
```

### JavaScript
```javascript
// Discover edge node
fetch('http://192.168.1.100:8000/api/v1/discover')
  .then(response => response.json())
  .then(data => {
    console.log('Connected to:', data.node_name);
    console.log('Capabilities:', data.capabilities);
  });
```

### Mobile App Integration
```dart
// Flutter/Dart example
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map<String, dynamic>> discoverEdgeNode(String edgeNodeIp) async {
  final response = await http.get(
    Uri.parse('http://$edgeNodeIp:8000/api/v1/discover')
  );
  
  if (response.statusCode == 200) {
    return json.decode(response.body);
  } else {
    throw Exception('Failed to discover edge node');
  }
}
```

## Deployment Notes

### Local Network
- Edge node should be on the same WiFi network as mobile devices
- Use mDNS/Bonjour for automatic discovery (future enhancement)
- Default port: 8000

### Network Configuration
- Ensure firewall allows inbound connections on port 8000
- For school deployments, configure WiFi router appropriately
- Consider using static IP for the edge node

### Monitoring
- Use `/health` endpoint for uptime monitoring
- Monitor service status for degradation detection
- Set up alerts for service failures

## Security Considerations

**Current Implementation** (Development):
- No authentication
- Open CORS policy
- HTTP (not HTTPS)

**Production Requirements**:
- [ ] Add authentication (API keys or JWT)
- [ ] Implement HTTPS with TLS certificates
- [ ] Restrict CORS to specific origins
- [ ] Add rate limiting
- [ ] Implement request logging
- [ ] Add input validation and sanitization

## Version History

### v1.0.0 (2026-02-16)
- Initial API implementation
- Service discovery endpoint
- Health check endpoint
- Basic API Gateway functionality
