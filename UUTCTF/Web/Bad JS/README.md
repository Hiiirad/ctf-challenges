**This challenge had a lot of steps which could be cooler than what I just did if everything could be written in one python script.**

My steps:
  1. Extract files from JS.7z
  2. Analyze JS.js file and extract all the hex codes with python (`get_flag.py`)
  3. Copy and paste hex codes to online decoders. Such as [link](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
  4. Some parts of result are base64, so I used [online converter](https://www.base64decode.org/).
  5. One of the base64 was `RmxhZyBpczogTUQ1KDEyNy4wLjAuMSk=` and decoded form of it was `Flag is: MD5(127.0.0.1)`.
  6. Done :)
