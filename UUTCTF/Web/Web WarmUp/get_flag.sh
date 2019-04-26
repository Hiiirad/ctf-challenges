#!/bin/bash
7z x WarmUp.7z
strings UUTCTF.htm | grep -oie "uutctf{.*}"
