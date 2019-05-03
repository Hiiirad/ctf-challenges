from base64 import b64decode
from re import findall
from binascii import hexlify

"""
import binascii
binascii.hexlify("\xee\x06@\x00\x00\x00\x00\x00")

bytes.fromhex("0x1dfea4").decode("utf-8")
"""

with open(file="JS.js", mode="r", encoding="utf-8") as f:
    codes = f.read()
    hex_codes = [findall(string=codes, pattern=r"(0x[0-9a-f]{1,}|(\\x[0-9a-f]{2}){1,})")]
    hex_codes = [str(index[0]) for index in hex_codes[0]]
    
print(hex_codes)