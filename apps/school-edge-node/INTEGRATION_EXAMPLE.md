# Integration Example for eZansiEdgeAI

This example shows how to integrate with the MaSf-vision Edge Node API.

## Quick Test

### 1. Start the Edge Node API
```bash
cd apps/school-edge-node
python api_server.py
```

### 2. Test from Python
```python
import requests

# Discover the edge node
edge_node_url = "http://localhost:8000"

# Check if API is available
try:
    response = requests.get(f"{edge_node_url}/api/v1/discover")
    if response.status_code == 200:
        node_info = response.json()
        print(f"✓ Connected to: {node_info['node_name']}")
        print(f"✓ Node ID: {node_info['node_id']}")
        print(f"✓ Status: {node_info['status']}")
        print(f"✓ Capabilities: {', '.join(node_info['capabilities'])}")
    else:
        print("✗ API not found")
except requests.exceptions.ConnectionError:
    print("✗ Cannot connect to edge node")
```

### 3. Test from Command Line
```bash
# Check API is available
curl http://localhost:8000/api/v1/discover

# Check health
curl http://localhost:8000/health

# List services
curl http://localhost:8000/api/v1/services
```

## Integration from eZansiEdgeAI Repository

### Discovery Pattern
```python
class EdgeNodeClient:
    """Client for MaSf-vision Edge Node API"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.node_info = None
    
    def discover(self):
        """Discover edge node and its capabilities"""
        try:
            response = requests.get(f"{self.base_url}/api/v1/discover")
            response.raise_for_status()
            self.node_info = response.json()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Edge node discovery failed: {e}")
            return False
    
    def is_available(self):
        """Check if edge node API is available"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def get_services(self):
        """Get list of available services"""
        response = requests.get(f"{self.base_url}/api/v1/services")
        response.raise_for_status()
        return response.json()

# Usage
client = EdgeNodeClient()
if client.discover():
    print("Edge node found!")
    services = client.get_services()
    print(f"Available services: {len(services['services'])}")
else:
    print("Edge node not available - falling back to mobile-only mode")
```

## Network Discovery

For automatic edge node discovery on a local network:

```python
import socket
import requests

def find_edge_nodes(port=8000, subnet="192.168.1"):
    """Scan local network for edge nodes"""
    found_nodes = []
    
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        try:
            response = requests.get(
                f"http://{ip}:{port}/api/v1/discover",
                timeout=0.5
            )
            if response.status_code == 200:
                node_info = response.json()
                found_nodes.append({
                    "ip": ip,
                    "info": node_info
                })
        except:
            continue
    
    return found_nodes

# Find all edge nodes on network
nodes = find_edge_nodes()
print(f"Found {len(nodes)} edge node(s)")
```

## Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Request successful
- `404 Not Found`: Endpoint doesn't exist
- `501 Not Implemented`: Service not yet implemented
- `500 Internal Server Error`: Server error

Example with error handling:
```python
try:
    response = requests.get(f"{edge_url}/api/v1/content/packages")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 501:
        print("Content distribution not yet available")
        # Fall back to alternative method
    else:
        raise
```

## Testing the Integration

Run this test script to verify integration:

```python
#!/usr/bin/env python3
import requests
import sys

def test_edge_node_api(base_url="http://localhost:8000"):
    """Test all API endpoints"""
    
    tests = [
        ("Root", "/"),
        ("Health", "/health"),
        ("Discover", "/api/v1/discover"),
        ("Services", "/api/v1/services"),
        ("Status", "/api/v1/status"),
    ]
    
    print(f"Testing Edge Node API at {base_url}\n")
    
    for name, endpoint in tests:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            if response.status_code == 200:
                print(f"✓ {name:15} - OK")
            else:
                print(f"✗ {name:15} - Failed ({response.status_code})")
        except Exception as e:
            print(f"✗ {name:15} - Error: {e}")
            return False
    
    print("\n✓ All tests passed!")
    return True

if __name__ == "__main__":
    success = test_edge_node_api()
    sys.exit(0 if success else 1)
```

## Next Steps

Once content distribution, model inference, and sync services are implemented, you'll be able to:

1. **Content Distribution**
   ```python
   # List available content packages
   packages = client.get("/api/v1/content/packages")
   
   # Download a specific package
   package = client.get(f"/api/v1/content/packages/{package_id}")
   ```

2. **Model Inference**
   ```python
   # Run inference on edge node
   result = client.post("/api/v1/inference", json={
       "model": "explanation-model",
       "input": "What is 2+2?"
   })
   ```

3. **Sync Coordination**
   ```python
   # Upload sync data
   client.post("/api/v1/sync/upload", json={
       "device_id": "mobile-001",
       "data": {...}
   })
   ```

For now, the discovery and health check endpoints provide the foundation for integration.
