#!/bin/bash
if [ $# -le 0 ]; then
  echo "Usage: test.sh [loop count]"
  exit 1
fi

for i in `seq 1 $1`
do
  /usr/local/bin/mjai-manue --name=NoName mjsonp://127.0.0.1:11600/0_0
  sleep 10
done
