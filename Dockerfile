FROM alpine:3.6

RUN apk add --update python3 py3-pip

EXPOSE 8080
RUN mkdir -p /opt/profileservice
ADD requirements.txt /opt/profileservice/
ADD profileservice/*.py /opt/profileservice/

WORKDIR /opt/profileservice
RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]