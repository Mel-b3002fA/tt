#!/bin/bash
# Kill whatever is using port 5000
lsof -ti:5000 | xargs kill -9 2>/dev/null

# Run your Flask server
python server.py
