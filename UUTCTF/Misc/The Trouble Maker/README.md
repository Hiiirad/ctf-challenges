**This was an easy challenge :)**

Steps to solve this challenge:

  1. I checked web objects and directories of our URL with `$dirb http://188.40.189.2:8001/`
  2. .git showed in our scan and we can analyze it with `git-dumper`
  3. `$python git-dumper.py http://188.40.189.2:8001/.git output/`
  4. `$git show`
  5. War string was there and we decoded it with our `get_flag.sh`
  6. Done :)
