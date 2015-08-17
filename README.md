# ctftrolol

Basedir is /var/www/html/

## LFI Vuln
LFI (file read): http://challs.campctf.ccc.ac:10119/?page=php://filter/convert.base64-encode/resource=info  
[PoC Script for Downloading Files](https://github.com/0x27/ctftrolol/blob/master/trolol_fileread.py)

## Key/Value Overwrite Vuln
PoC coming.

## Saucery
* index.php - contains [variable overwrite vuln](https://github.com/0x27/ctftrolol/blob/master/index.php#L4,L7) and [LFI vuln (limited to .php files)](https://github.com/0x27/ctftrolol/blob/master/index.php#L9). Also has [hardcoded password hash](https://github.com/0x27/ctftrolol/blob/master/index.php#L2)
* info.php - phpinfo file
* login.php - Handles login logic. Displays a [false flag on successful login/bypass](https://github.com/0x27/ctftrolol/blob/master/login.php#L5). Vars can be overwritten using the key/balue bug in index.php
* main.php - Just some links, maps the whole thing together.

## XSports
* trolol_fileread.py - read .php files from server

Please add notes as you find shit :)
