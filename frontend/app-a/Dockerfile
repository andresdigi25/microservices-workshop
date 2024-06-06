FROM node:20.13.1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install -g @angular/cli@18.0.3

RUN npm install

EXPOSE 8081

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "8081"]
