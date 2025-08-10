# UCR Course Connect

### Backend

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/uvicorn-1B1F23?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-0C234B?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Google Sheets API](https://img.shields.io/badge/google_sheets_API-34A853?style=for-the-badge&logo=google&logoColor=white)

### Frontend

![React](https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/typescript-%23407ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Axios](https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)
![Node.js](https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)

### Dev Tools & CI/CD

![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![ESLint](https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white)
![Prettier](https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E)
![Figma](https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)

## About

A web app to help students search and review UCR courses, using the popular UCR Course Database Google Sheets as a live data source for courses and reviews.
The platform offers advanced course filtering for easy navigation, supports user-submitted reviews and ratings to help students make informed decisions,
and features a mobile-optimized responsive design for seamless use on any device.

## Development Features

- Periodic backend data refresh using threading and periodic Google Sheets sync
- Fast, reactive frontend for search queries
- Dockerized backend and frontend for easy deployment
- CI/CD pipeline using GitHub Actions
- Styling and UI optimized with Tailwind and Vite

## How it Fits Together

- Backend loads course data from Google Sheets and exposes API endpoints
- Frontend queries backend endpoints using Axios based on user input from the search bar
- Docker ensures isolated environments for backend and frontend
- CI/CD automates testing and deployment pipelines
- AWS hosts the deployed app
- Figma supports UI/UX design and prototyping

## Installations & Running Instructions

### Backend

```bash
# Prerequisites:
Python 3.10+

# Install Dependencies:
pip install -r requirements.txt

# Run Backend Server:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Test Backend Endpoints:
http://localhost:8000
```

### Frontend

```bash
# Prerequisites:
Node.js (v16+)

# Install Dependencies:
cd frontend
npm install

# Run Frontend Server:
npm run dev

# Open App:
http://localhost:5173

# Build for Production:
npm run build
```

### Docker (Backend and Frontend)

```bash
# Build Docker Images::
docker build -t your-backend-image-name backend/
docker build -t your-frontend-image-name frontend/

# Run with Docker Compose::
docker-compose up --build

# Access the App:
Backend API: http://localhost:8000
Frontend UI: http://localhost:3000

# Stop Containers:
docker-compose down
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
