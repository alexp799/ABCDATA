#!/usr/bin/bash

for f in $(find . -name 'r*'); do 7z x $f; done
