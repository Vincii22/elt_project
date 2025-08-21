FROM python:3.12-slim

# Install PostgreSQL 17 client (pg_dump, psql, pg_isready)
RUN apt-get update && apt-get install -y curl gnupg lsb-release && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/pgdg.gpg && \
    apt-get update && apt-get install -y postgresql-client-17 cron && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY start.sh /app/start.sh
COPY elt_script.py .

RUN echo "0 15 * * * python /app/elt_script.py" | crontab -
CMD ["python", "elt_script.py"]
