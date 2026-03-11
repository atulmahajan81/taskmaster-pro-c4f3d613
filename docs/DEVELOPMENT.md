# Development

## Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/example/taskmaster-pro.git
   cd taskmaster-pro
   ```

2. **Install Dependencies**
   - Backend (Python Dependencies)
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - Frontend (Node.js Dependencies)
     ```bash
     cd frontend
     npm install
     ```

3. **Run the Application Locally**
   ```bash
   docker-compose up --build
   ```

## Running Tests

- **Backend Tests**
  ```bash
  cd backend
  pytest
  ```

- **Frontend Tests**
  ```bash
  cd frontend
  npm test
  ```

## Code Structure

- **Frontend**: Located in the `frontend` directory, structured as a Next.js application.
- **Backend**: Located in the `backend` directory, structured as a FastAPI application.

## Contributing Guide

- Fork the repository.
- Create a new branch (`git checkout -b feature/your-feature-name`).
- Commit your changes (`git commit -m 'Add new feature'`).
- Push to the branch (`git push origin feature/your-feature-name`).
- Open a pull request.