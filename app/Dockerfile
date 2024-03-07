FROM ubuntu:latest

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install numpy 

WORKDIR /usr/app/rand-generator

COPY ./main.py .

CMD ["python3", "./main.py"]