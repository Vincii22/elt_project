import subprocess
import time
import os
import sys

def wait_for_postgres(host, db, user="postgres", port="5432", max_retries=20, delay_seconds=3):
    retries = 0
    while retries < max_retries:
        try:
            # Just connectivity probe; pg_isready doesn’t need a password.
            subprocess.run(
                ["pg_isready", "-h", host, "-p", port, "-U", user, "-d", db],
                check=True, capture_output=True, text=True
            )
            print(f" {host}/{db} is ready")
            return True
        except subprocess.CalledProcessError as e:
            retries += 1
            print(f"Error connecting to {host}: {e}")
            print(f"Retrying in {delay_seconds} seconds... (Attempt {retries}/{max_retries})")
            time.sleep(delay_seconds)
    print(f" Max retries reached. {host}/{db} not ready.")
    return False

print("Waiting for databases...")
if not wait_for_postgres("source_postgres", "source_db"): sys.exit(1)
if not wait_for_postgres("destination_postgres", "destination_db"): sys.exit(1)

print("Starting ELT Script...")

source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'redblood12',
    'host': 'source_postgres',
    'port': '5432',
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password': 'redblood12',
    'host': 'destination_postgres',
    'port': '5432',
}

dump_file = "data_dump.sql"

dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-p', source_config['port'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', dump_file,
    '-w'
]

env_src = os.environ.copy()
env_src['PGPASSWORD'] = source_config['password']

print(" Dumping source_db ...")
subprocess.run(dump_command, env=env_src, check=True)


if not (os.path.exists(dump_file) and os.path.getsize(dump_file) > 0):
    print(" Dump file is empty or missing.")
    sys.exit(1)

load_command = [
    'psql',
    '-h', destination_config['host'],
    '-p', destination_config['port'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', dump_file,
]

env_dst = os.environ.copy()
env_dst['PGPASSWORD'] = destination_config['password']

print(" Loading into destination_db ...")
subprocess.run(load_command, env=env_dst, check=True)

print("ELT complete.")
