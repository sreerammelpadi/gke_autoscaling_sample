#!/bin/bash
cd "$(dirname "$0")"

# Install dependencies if not already installed
if ! python3 -c "import aiohttp" 2>/dev/null; then
    apt-get update && apt-get install -y python3-pip
    pip3 install -r producer/requirements.txt
fi

# Run the producer script
python3 producer/main.py
