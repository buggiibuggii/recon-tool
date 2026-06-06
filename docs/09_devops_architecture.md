# 9. DevOps Architecture

## Stack

- API: FastAPI container.
- Database: PostgreSQL 16.
- Cache/queues: Redis.
- Vector database: ChromaDB.
- Storage: S3 in AWS Mumbai.
- Reverse proxy: nginx.
- Monitoring: Prometheus and Grafana-ready config.

## Deployment

CI validates backend schema/tests and frontend TypeScript. Production deployments should use ECS/Fargate or EKS in `ap-south-1`, private subnets for databases, S3 bucket encryption, AWS WAF, CloudWatch logs, and automated backups.

## Backup and disaster recovery

- PostgreSQL PITR with daily snapshots and WAL archiving.
- S3 versioning and lifecycle rules.
- Chroma collection snapshots after ingestion jobs.
- Quarterly restore drills and runbook validation.
