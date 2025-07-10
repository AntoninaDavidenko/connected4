# Connected4 - Real-Time Multiplayer Connect Four Game

A full-stack multiplayer Connect Four game with real-time functionality, built with modern web technologies. Two players can compete via shared links with comprehensive game tracking and customization options. 

![Connected4 Game](https://img.shields.io/badge/Game-Connect%20Four-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=next.js&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

## 🎮 Game Preview
<img width="1351" height="810" alt="image" src="https://github.com/user-attachments/assets/3668e9eb-3e01-45c7-ba24-269fd7c6f2df" />
<img width="1345" height="826" alt="image 1png" src="https://github.com/user-attachments/assets/acce6895-02e4-467c-81b3-9ee4089a783b" />


## 🎯 Features

### Core Gameplay
- **Real-time multiplayer** functionality via WebSocket connections
- **Shared game links** - players can join games through unique URLs
- **Turn-based gameplay** with automatic player switching
- **Win condition detection** and draw state handling
- **Game replay functionality** with complete match history

### User Experience
- **Player customization** with name selection
- **Dual theme support** - light and dark modes
- **Responsive UI design** with visual feedback for moves
- **Cross-browser compatibility** for seamless gameplay
- **Real-time game state updates** for both players

### Data Management
- **MongoDB integration** for persistent game history
- **Comprehensive game tracking** with match statistics
- **Session management** for active games
- **Performance optimization** with efficient data queries

## 🛠️ Technology Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **MongoDB** - NoSQL database for game data storage
- **WebSocket** - Real-time communication protocol
- **Python 3.11+** - Core programming language

### Frontend
- **Next.js** - React-based frontend framework
- **TailwindCSS** - Utility-first CSS framework
- **JavaScript/TypeScript** - Frontend logic implementation
- **Responsive Design** - Mobile-first approach

### DevOps
- **Docker** - Containerization for easy deployment
- **Docker Compose** - Multi-container application management

## 🚀 Installation and Setup

### Prerequisites
- Python 3.11 or higher
- Node.js 18.0 or higher
- MongoDB (local installation or MongoDB Atlas)
- Docker (optional, for containerized deployment)

### Local Development Setup

#### 1. Clone the repository
```bash
git clone https://github.com/AntoninaDavidenko/connected4.git
cd connected4
```

#### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your MongoDB connection string
```

#### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Configure environment variables
cp .env.local.example .env.local
# Edit .env.local with your API endpoint
```

#### 4. Database Setup
```bash
# Start MongoDB (if running locally)
mongod

# Or use Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

#### 5. Run the application
```bash
# Start backend server
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Start frontend development server
cd frontend
npm run dev
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

## 🎮 How to Play

1. **Start a Game**: Navigate to the application and create a new game
2. **Share Link**: Copy the generated game link and share it with another player
3. **Join Game**: The second player clicks the shared link to join
4. **Play**: Players take turns dropping pieces into the 7x6 grid
5. **Win**: Connect four pieces horizontally, vertically, or diagonally to win
6. **Replay**: View game history and replay previous matches

## 🏗️ Project Structure

```
connected4/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic
│   │   └── websocket/       # WebSocket handlers
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Next.js pages
│   │   ├── hooks/           # Custom React hooks
│   │   └── utils/           # Utility functions
│   ├── public/
│   └── package.json
├── docker-compose.yml
└── README.md
```

## 🔧 API Endpoints

### Game Management
- `POST /games` - Create new game
- `GET /games/{game_id}` - Get game details
- `PUT /games/{game_id}/join` - Join existing game
- `GET /games/{game_id}/history` - Get game history

### WebSocket Events
- `connect` - Player connection
- `move` - Player move
- `game_state` - Game state updates
- `game_end` - Game completion

## 🎨 Customization Options

### Themes
- **Light Mode**: Clean, bright interface
- **Dark Mode**: Modern, dark interface with reduced eye strain

### Player Settings
- **Custom player names**: Players can set personalized names for identification

## 🧪 Testing

```bash
# Run backend tests
cd backend
pytest

# Run frontend tests
cd frontend
npm test
```

---

*Developed as part of a full-stack development portfolio project (October 2024 - December 2024)*
