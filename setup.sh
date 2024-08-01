#!/bin/bash

# Create main project directory


# Create app directory and its subdirectories
mkdir -p app/{api/endpoints,core,db,models,schemas,services}

# Create test directory
mkdir -p tests

# Create empty Python files
touch app/__init__.py app/main.py
touch app/api/__init__.py app/api/endpoints/__init__.py app/api/endpoints/pipeline.py
touch app/core/__init__.py app/core/config.py app/core/logging.py
touch app/db/__init__.py app/db/database.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/services/__init__.py app/services/data_pipeline.py

# Create test files
touch tests/__init__.py tests/test_api.py tests/test_services.py

# Create root level files
touch .env .gitignore Dockerfile docker-compose.yml requirements.txt README.md

echo "FastAPI project structure created successfully!"