FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS fast-uv

WORKDIR /app

COPY pyproject.toml pyproject.toml

# RUN uv sync --no-dev --no-cache --no-install-project
RUN uv pip install --system --no-cache-dir .


FROM python:3.13-slim AS fast-server

# Copy installed site-packages from build stage
COPY --from=fast-uv /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

WORKDIR /app

RUN adduser --disabled-password --gecos '' user \
    && mkdir /app/logs \
    && chown -R user:user /app/logs

USER user
# Copy application code
COPY --chown=user:user . .

CMD [ "python", "main.py" ]
