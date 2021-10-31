#!/bin/bash

if [ ! -e ./venv ]; then
  virtualenv -p python3 venv
  source venv/bin/activate

  if [ -e requirements.txt ]; then
    pip3 install -r requirements.txt
  fi

  if [ -e dev-requirements.txt ]; then
    pip3 install -r dev-requirements.txt
  fi
fi

source venv/bin/activate


