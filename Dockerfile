FROM python:3.10
WORKDIR /src
COPY ./src /src
RUN pip3 install -r requirements.txt
