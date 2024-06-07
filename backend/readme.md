docker build -t service_a .
docker run -p 5000:5000 service_a

docker build -t service_b .
docker run -p 5001:5001 service_b

docker build -t service_c .
docker run -p 5002:5002 service_c