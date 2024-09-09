# DataPipeline

## Project Objectives

This project involves building a comprehensive data warehouse system. The main objective is to collect and integrate data from multiple sources into a MySQL-based data warehouse engine. The data sources include PostgreSQL, CSV files, Kafka streams, RabbitMQ, APIs, and even non-relational databases like MongoDB. The system is designed to handle diverse data types, ensuring efficient storage, processing, and retrieval to support data-driven decision-making and analysis. By consolidating all these different data formats, the project aims to provide a unified platform for data management and reporting.

## Project Flow

Firstly, we will ingest and store data from various resources into the lakehouse architecture. At this stage, we only store the raw, untransformed data to ensure that the original information is retained for future processing. By preserving this raw data, we create flexibility for various analytical use cases. Following that, we leverage the raw data for reporting purposes. Using ELT (Extract, Load, Transform) processes, we transform the raw data to meet specific business requirements. This transformed data is then used to create visualizations, such as graphs and pivot tables, which provide actionable insights tailored to the organization's needs. Additionally, we ensure that this transformation aligns with key business metrics and objectives, enabling efficient decision-making.
