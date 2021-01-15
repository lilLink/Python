import cgi
import cgitb
import time
import os

print ("Content-type: text/html\n\n")


form = cgi.FieldStorage()
first = int(form.getfirst("first_num", 1))
second = int(form.getfirst("second_num", 1))

while first != 0 and second != 0:
    if first > second:
        first %= second
    else:
        second %= first

gcd = first + second




print ("<!DOCTYPE html>")
print ('<html lang="en">')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>N-th simple</title>')
print ('</head>')
print ('<body>')
print ('<p>')
print ('Answer: {0}'.format(gcd))
print ('</p>')
print ('<p>')
print ('</p>')
print ('</body>')
print ('</html>')