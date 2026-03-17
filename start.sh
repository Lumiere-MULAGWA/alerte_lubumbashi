#!/bin/bash
export PORT=${PORT:-8000}
exec
uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload