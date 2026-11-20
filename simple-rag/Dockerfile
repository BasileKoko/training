# Start with Python 3.12 slim on Debian
FROM python:3.12-slim

# Copy the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Configure uv for container builds:
# - Compile bytecode for faster startup
# - Copy files instead of symlinking across cache mounts
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install pinned dependencies from pyproject.toml & uv.lock
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev

# Copy your application code (app/, rag/, config.py, docs/, etc.)
COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"

# Point to app/chat.py
CMD ["python", "-m", "app.chat"]