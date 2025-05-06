$foo = docker ps -a | grep -w log-ingestion-api|awk '{print $1}'
docker rm -f $foo
docker build -t log-ingestion-api:0.1 .
docker run -p 8000:8000 log-ingestion-api:0.1
