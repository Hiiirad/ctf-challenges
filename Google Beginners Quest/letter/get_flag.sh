#!/bin/bash

unzip letter.zip
pdftotext challenge.pdf
cat challenge.txt | grep -i "ctf" | rev | cut -d " " -f 1 | rev
