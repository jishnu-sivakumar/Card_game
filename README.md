# 🃏 PyLAN Cards

A Python-based multiplayer card game engineered for local area networks (LAN/TCP). Built with a decoupled client-server architecture, it utilizes raw TCP sockets for real-time state synchronization and `customtkinter` for a modern, responsive graphical interface.

## 🏗️ System Architecture

This project employs a dual-server model to handle different phases of the network lifecycle:

* **Initialization Server (`init_server.py`):** Acts as the handshake and lobby manager. It initializes player connections, assigns UUIDs/names, and distributes the initial card decks securely.
* **Game Server (`game_server.py`):** The real-time physics and logic engine. It maintains the authoritative game state and handles all active gameplay interactions and broadcasts.

### Client Components

* `prototype.py`: The core game logic and state machine (can be executed via CLI for headless testing).
* `init_client.py`: The networking module responsible for the initial server handshake.
* `prototype_round_client.py`: The round-resolution client (currently in active development).
* `frontend_custom.py`: The main GUI application window.

## ⚙️ Prerequisites & Installation

Ensure you have Python 3.8+ installed. The GUI requires the following dependencies:

```bash
pip install customtkinter
pip install pillow

```

## 🚀 Execution Guide

To launch the environment locally, you must initialize the servers before connecting the clients.

1. **Start the Initialization Server:**
```bash
python init_server.py

```


2. **Start the Game Server:**
```bash
python game_server.py

```


3. **Launch Client Instances (Run on player machines):**
```bash
python frontend_custom.py

```



## 🗺️ Development Roadmap

* [ ] **Server Unification:** Merge the Initialization and Game servers into a single multiplexed asynchronous server.
* [ ] **Lobby System:** Implement a UI for players to create and join specific room codes.
* [ ] **Reconnection Protocol:** Allow players to seamlessly rejoin a match if their TCP connection drops.

---

### Professor's Domain Suggestions

In the realm of professional multiplayer game development, handling state purely over raw sockets can quickly become a tangled web. As you continue refining this project, I highly recommend exploring these widely used concepts:

1. **Message Framing:** TCP is a stream protocol, not a message protocol. To prevent data corruption (like your previous `EOFError`), prepend all your pickled byte-streams with a fixed-length header that dictates the exact size of the incoming payload.
2. **Single Multiplexed Server:** Running two separate servers for one game introduces complex synchronization challenges. The industry standard is to use a single server utilizing `select` or Python's `asyncio`. The server handles everything, but simply moves players between a "Lobby State" and a "Game State."
3. **Authoritative Server Model:** Never trust the client. The UI (`frontend_custom.py`) should only send "Attempt to play Card X" to the server. The server must validate if the move is legal, and then broadcast "Card X was played" back to all clients to update their screens.
