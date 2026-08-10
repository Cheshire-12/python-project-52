#!/usr/bin/env bash

set -o errexit

echo "Downloading uv..."
curl --proto "=https" -LsSf https://astral.sh | sh
source $HOME/.local/bin/env

echo "Installing project dependencies (production only)..."
make install-prod

echo "Collecting static files..."
make collectstatic

echo "Running database migrations..."
make migrate

echo "Compiling messages..."
make compilemessages

echo "Build successful!"