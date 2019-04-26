#!/bin/bash
strings Layers.jpg | grep -oe "uutctf{.*}" | cut -d '"' -f 1
