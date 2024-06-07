FROM python:3.9.16-slim-buster

WORKDIR /usr/src/app
ADD . ./

RUN apt-get update
RUN apt-get install -y gcc libc-dev unixodbc-dev g++ apt-transport-https libsnappy-dev libpq-dev libz-dev libjpeg-dev curl unzip libxrender1 libxtst6 libfontconfig1
RUN pip install --upgrade pip

RUN pip install -r requirements.txt 



EXPOSE 5002
# Run app.py when the container launches
CMD ["python", "main.py"]