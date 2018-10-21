#!/bin/sh

IFS=$'\n'
for font in $(cat google-fonts.txt); do
    wget "http://fonts.google.com/download?family=$font" -O "../fonts/${font// /-}.zip"
done