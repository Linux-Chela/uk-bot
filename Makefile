.PHONY: setup install run dev clean help activate

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
UVICORN = $(VENV)/bin/uvicorn

help:
	@echo "Available commands:"
	@echo "  make setup      - Create virtual environment"
	@echo "  make install    - Create venv and install dependencies"
	@echo "  make activate   - Show command to activate virtual environment"
	@echo "  make run        - Run the FastAPI application"
	@echo "  make dev        - Run in development mode with auto-reload"
	@echo "  make clean      - Remove Python cache files and virtual environment"
	@echo "  make help       - Show this help message"
	@echo ""
	@echo "Quick start:"
	@echo "  1. make install"
	@echo "  2. source venv/bin/activate"
	@echo "  3. make dev"

setup:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Virtual environment created successfully!"
	@echo "To activate it, run: source $(VENV)/bin/activate"

install: setup
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Installation complete!"
	@echo "To activate the virtual environment, run: source $(VENV)/bin/activate"

activate:
	@echo "To activate the virtual environment, run:"
	@echo "  source $(VENV)/bin/activate"

run:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	$(PYTHON) run.py

dev:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	$(UVICORN) app.main:app --reload --host 0.0.0.0 --port 8000

clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	rm -rf $(VENV)
	@echo "Cleanup complete!"
