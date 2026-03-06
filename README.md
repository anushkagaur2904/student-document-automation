# Student Document Automation System

An AI-powered system that processes handwritten student applications and automatically updates Excel records or generates Word documents.

---

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Accessing the Upload Page

### On Desktop (same machine as server)
```
http://127.0.0.1:8000/upload-page
```

### On Phone or other devices (must be on same WiFi)
```
http://YOUR_LAPTOP_IP:8000/upload-page
```
To find your laptop IP, run this in PowerShell:
```powershell
ipconfig
```
Look for **IPv4 Address** under **Wireless LAN adapter Wi-Fi**.

Note : **Moblie Data** should be **OFF** while testing.
