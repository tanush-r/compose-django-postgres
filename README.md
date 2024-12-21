# Docker Compose Basics: Django with Postgres

This project uses Docker Compose to set up a development environment with PostgreSQL database and Django application.

## Services

### Database Service (`db`)
- PostgreSQL database running on port 5432
- Database name: `sampledb`
- User: `sampleuser`
- Uses persistent volume storage (`db-vol`)

### Django Application (`django`)
- Built from the Dockerfile in `./backend` directory
- Runs on port 8000
- Connects to the PostgreSQL database
- Depends on database service to be running first

## Getting Started

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository and navigate to the project directory.

3. Start the services:
```bash
docker-compose up
```

4. Access the Django application at:
```
http://localhost:8000
```

5. To stop the services:
```bash
docker-compose down
```

## Environment Variables

The following environment variables are configured for both services:
- `POSTGRES_DB`: sampledb
- `POSTGRES_USER`: sampleuser
- `POSTGRES_PASSWORD`: samplepassword

## Volumes

The database uses a named volume `db-vol` to persist data between container restarts.

## Notes
- Make sure no other services are running on ports 5432 and 8000
- The database data will persist even after stopping the containers
- To completely reset the database, you'll need to remove the volume:
```bash
docker-compose down -v
```