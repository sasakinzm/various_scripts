#!/bin/bash
IP=`cat ./host_list.txt`
while read line
do
  ping $line -c 1 >> /dev/null &> /dev/null
  ret=$?
  if [ $ret -eq 0 ] ; then
    echo $line" 〇 OK!!!!"
  else
    echo $line" × NG...."
  fi
done << FILE
$IP
FILE
