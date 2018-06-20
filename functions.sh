#!/bin/bash

check_directory() {
if [ ! -d $1 ]
then
  mkdir $1
  return 1
else
  return 0
fi
}

#mutect_calling() {
#
#}