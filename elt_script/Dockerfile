FROM python:3.12-slim

# Install PostgreSQL 17 client (pg_dump, psql, pg_isready)
RUN apt-get update && apt-get install -y curl gnupg lsb-release && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/pgdg.gpg && \
    apt-get update && apt-get install -y postgresql-client-17 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR .
COPY elt_script.py .

CMD ["python", "elt_script.py"]
