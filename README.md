🚀 Custom ELT Project

This repository demonstrates a modern Extract, Load, Transform (ELT) pipeline using a real-world data engineering stack. The project leverages Docker, Airflow, Airbyte, dbt, cron, PostgreSQL, and Python scripting to orchestrate ingestion, transformation, and automation.

📂 Repository Structure

docker-compose.yaml – Orchestrates all services (Airflow, Airbyte, PostgreSQL, etc.)

airflow/ – Contains DAGs and supporting files for orchestrating the ELT pipeline

dags/elt_pipeline_dag.py – Airflow DAG defining the pipeline workflow

airbyte/ – Configuration for data ingestion (e.g., syncing source PostgreSQL → destination PostgreSQL)

dbt_project/ – dbt models, seeds, and configs for SQL-based transformations

scripts/ – Custom Python or cron jobs to support extra automation or data checks

source_db_init/init.sql – Initializes the source PostgreSQL database with sample tables and data

⚙️ Tools Used

Docker & Docker Compose → Containerize and run all services together

PostgreSQL → Used as both source and destination databases

Airbyte → Handles Extract + Load (syncs data from source PostgreSQL → destination PostgreSQL)

dbt → Handles Transform (runs SQL models inside the destination warehouse)

Airflow → Orchestrates the pipeline (e.g., trigger Airbyte sync → run dbt models)

cron → Lightweight job scheduling for recurring scripts or health checks

Python → Custom scripting for automation or data validation

🔄 How It Works

Source Database Initialization

The source_postgres container is populated with sample data (tables, users, films, categories, etc.) from init.sql.

Data Ingestion with Airbyte

Airbyte is configured to extract data from source_postgres and load it into destination_postgres.

Pipeline Orchestration with Airflow

Airflow DAG (elt_pipeline_dag.py) orchestrates:

Trigger Airbyte sync (Extract + Load)

Run dbt models (Transform)

Optionally run Python validation scripts

Transformations with dbt

dbt models clean and transform the raw data into analytics-ready tables.

Scheduling

Pipelines can be scheduled via Airflow or cron jobs for recurring runs.

🚀 Getting Started
Prerequisites

Docker & Docker Compose installed on your machine

Setup
# Clone repository
git clone https://github.com/your-username/custom-elt-project.git
cd custom-elt-project

# Start all services
docker-compose up

Accessing Services

Airflow UI → http://localhost:8080

Airbyte UI → http://localhost:8000

Source PostgreSQL → port 5433

Destination PostgreSQL → port 5434

✅ Workflow Summary

Airbyte extracts data from source_postgres

Airbyte loads raw data into destination_postgres

Airflow triggers the pipeline and orchestrates tasks

dbt runs SQL models to transform the raw data into clean, analytics-ready tables

Python scripts / cron jobs handle any extra automation or checks

📊 Example Use Case

Imagine a movie database system:

Source DB contains raw user, film, and actor tables.

Airbyte syncs this into the destination DB.

dbt creates transformed tables like dim_users, dim_films, and fact_user_activity.

Airflow ensures everything runs in the right order daily at midnight.