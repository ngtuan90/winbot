# WINBOT -- Raspberry Pi WebSocket Robot Control (Xbox Controller)

This project allows you to control a Raspberry Pi–based robot remotely using an **Xbox controller/Keyboard on a laptop**, communicating over a **WebSocket connection**.
---

## 🎮 Control Scheme

Using the **Xbox controller left analog stick**:

* Stick UP → Forward
* Stick DOWN → Backward
* Stick LEFT → Left
* Stick RIGHT → Right
* Stick CENTER → Stop

---

## 🧠 Architecture

```
Xbox Controller
      ↓
Laptop (WebSocket Client)
      ↓
Raspberry Pi (WebSocket Server)
      ↓
winbot.py (motor control)
```
---

## ⚙️ Requirements

### Raspberry Pi

* Python 3.8+
* `websockets`

### Laptop

* Python 3.8+
* `websockets`
* `pygame`
* Xbox controller (USB or Bluetooth)

---

## 📦 Installation

### Install dependencies (Pi + Laptop)

```bash
pip install websockets pygame
```

---

## 🖥 Raspberry Pi: WebSocket Server

### `server.py`

* Runs on the Raspberry Pi
* Receives direction commands over WebSocket
* Calls motor functions in `winbot.py`

Start the server:

```bash
python3 server.py
```

The server listens on port `8765`.

---

## 💻 Laptop: Xbox Controller Client

### `xbox_client.py`

* Reads Xbox controller input
* Sends direction commands to Raspberry Pi
* Uses only left stick directions

Run on laptop:

```bash
python3 xbox_client.py
```

Make sure to update the Raspberry Pi IP address inside the file:

```python
PI_IP = "192.168.1.100"
```

---

## 🔁 Auto Start on Boot (Optional)

Use `systemd` to start `server.py` automatically on Raspberry Pi boot.

---

## ✅ Summary

* Xbox controller on laptop
* WebSocket communication
* Simple directional control
* Low latency
* Easy to extend

---

