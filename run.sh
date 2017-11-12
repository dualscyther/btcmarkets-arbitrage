#!/bin/bash

while true; do
  clear;
  python2 main.py | sort -nr;
  sleep 5;
done


