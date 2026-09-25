.PHONY: test lint run-mcp run-webhook help

help:
	@echo "Available commands:"
	@echo "  make test        - Run all pytest unit tests with verbose output"
	@echo "  make lint        - Run ruff/flake8 style and syntax checks"
	@echo "  make run-mcp     - Start the Model Context Protocol (MCP) server"
	@echo "  make run-webhook - Start the FastAPI webhook receiver service"

test:
	python3 -m pytest tests/ -v

lint:
	python3 -m pip install ruff -q
	ruff check core/ tests/

run-mcp:
	python3 gtm-os/mcp/speed-to-lead/speed_to_lead_server.py

run-webhook:
	uvicorn core.api.webhook:app --reload --port 8000
