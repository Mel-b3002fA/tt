#!/bin/bash

PORT=5001

PID=$(lsof -ti tcp:$PORT)

if [ -n "$PID" ]; then
  echo "Killing process on port $PORT (PID $PID)..."
  kill -9 $PID
fi

echo "Starting server on port $PORT..."
python server.py
