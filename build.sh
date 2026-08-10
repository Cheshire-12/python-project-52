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

set -o errexit

if command -v uv >/dev/null 2>&1; then
    echo "uv already installed: $(uv --version)"
else
    echo "uv not found, download and install..."
    curl --proto "=https" -LsSf https://astral.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi
