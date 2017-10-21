#!/usr/bin/env bash

echo "Enter 'l' for deploying locally, 's' for online."
read opt

if [ "$opt" = 'l' ]; then
    # Run server.
    python3 suggestion_server.py
fi
if [ "$opt" = 's' ]; then
    python3 suggestion_server.py -p 5000 &
    ngrok http 5000
fi
