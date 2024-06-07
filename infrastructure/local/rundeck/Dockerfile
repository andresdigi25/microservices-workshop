FROM rundeck/rundeck:5.3.0

ENV RUNDECK_GRAILS_URL http://localhost:4440
ENV RUNDECK_SERVER_FORWARDED true

USER root

RUN apt-get update
RUN apt-get install -y curl unzip python3 python3-pip python3.10-venv libgbm-dev libasound2 libatk-bridge2.0-0 libgtk-4-1 libnss3 xdg-utils wget

RUN wget -q -O chrome-linux64.zip https://bit.ly/chrome-linux64-121-0-6167-85
RUN wget -q -O chromedriver-linux64.zip https://bit.ly/chromedriver-linux64-121-0-6167-85

RUN unzip chrome-linux64.zip
RUN rm chrome-linux64.zip
RUN mv chrome-linux64 /opt/chrome/
RUN ln -s /opt/chrome/chrome /usr/local/bin/google-chrome

RUN unzip -j chromedriver-linux64.zip chromedriver-linux64/chromedriver
RUN rm chromedriver-linux64.zip
RUN mv chromedriver /usr/local/bin/

USER rundeck

COPY test/selenium/requirements.txt .

RUN python3 -m venv /home/rundeck/selenium-env &&  \
    source /home/rundeck/selenium-env/bin/activate && \
    pip install -r requirements.txt

EXPOSE 4440