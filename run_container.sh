#!/bin/bash

#Script automate build container
CONTAINER=pointbreak/profile-service
NAME=profile-service
LOG=./run_container.log

killer() {
  #killer container
  echo "-- Stopping and removing container..."
  docker kill $NAME 2> /dev/null >> $LOG
  docker rm $NAME -f 2> /dev/null >> $LOG
  echo "--- Done."
}

build() {
  #Build container
  echo "-- Docker build $CONTAINER..."
  echo "** It can take some time, please wait..."
  docker build -t $CONTAINER . >> $LOG
  echo "--- Done."
}

run(){
  echo "-- Starting $CONTAINER..."
  docker run --name $NAME -p 8080:8080 -d $CONTAINER >> $LOG 2>&1
  echo "--- Done."
}

start() {
  killer
  build
  run
}

stop() {
  killer
}

tests() {
  docker exec -it $NAME python3 /opt/profileservice/tests.py
}

case "$1" in
    start)   start ;;
    stop)    stop ;;
    tests)   tests ;;
    *) echo "usage: $0 start|stop|tests" >&2
       exit 1
       ;;
esac