#!/bin/bash

TASK=$1

if [ -z ${TASK} ]; then
  echo "Usage: make <init|build>"
  exit 1;
fi

init() {
  python3 -m virtualenv venv
  . venv/bin/activate
  which python3
  pip install -r requirements.txt
}

build() {
  python3 package.py
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
