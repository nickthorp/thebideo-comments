#!/bin/bash

TASK=$1
ACTIVATE_DIR='venv/bin/activate'

if [ -z ${TASK} ]; then
  echo "Usage: make <init|build>"
  exit 1;
fi

init() {
  python3 -m virtualenv venv
  . ${ACTIVATE_DIR}
  pip install vdist
}

build() {
  . ${ACTIVATE_DIR}
  docker ps -a
  python3 packager2.py
}

case "$TASK" in
  "init")
    init
    ;;
  "build")
    build
    ;;
  *)
    echo "Try again.."
    ;;
esac
