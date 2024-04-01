#!/bin/bash

start_services() {

# Command to bring up Docker containers using docker-compose
docker-compose up -d

# Change directory to 'app'
cd app || exit 1

# Activate poetry shell and run the engine
. "$(poetry env info --path)/bin/activate" || exit 1
nohup python3 engine_run.py > engine_run.log 2>&1 &
echo "Services started successfully."
}


stop_services() {
    pkill -f "python3 engine_run.py"
    docker-compose down
    echo "Services stopped successfully."
}

# Check the argument
if [ "$1" == "start" ]; then
    start_services
elif [ "$1" == "stop" ]; then
    stop_services
else
    echo "Usage: $0 [start|stop]"
    exit 1
fi