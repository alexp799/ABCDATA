#!/usr/bin/bash

for i in $(find . -name '0*/'); do cp -r $i /home/fidesys/ABCDATA/data_processing/data; done
