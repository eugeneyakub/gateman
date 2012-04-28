#!/usr/bin/env python

import sys
from subprocess import call, Popen, PIPE


import fcntl, os


import re

# make stdin a non-blocking file
fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

_path =  '/tmp/request.tex'
_file = open(_path, 'w')
# user input handling thread
_length = 0
while 1:
    try:
        input = sys.stdin.readline()
        if re.findall('Content-Length', input):
            _length = int(input.split(' ')[1])
    except:
        continue
    if (len(input) <= 2): break

_file.write(sys.stdin.read(_length))
_file.close()



print 'HTTP/1.0 200 OK'
print 'Access-Control-Allow-Origin: *'
print 'Access-Control-Allow-Headers: X-Prototype-Version, X-Requested-With, Content-type, Accept'
print 'Access-Control-Allow-Methods:  GET, POST, OPTIONS, PUT'
print 'Content-Type: text/html; charset=UTF-8'
print 'Content-Language: en-US'
print '\n\n'
print '<html><body><p>'+'aawdwdwdwdwdwd'+'</p></body></html>'


import os
os.chdir('/tmp')
my_env = os.environ

#my_env["TFMFONTS"] = "/usr/share/texmf-texlive/fonts/tfm:/usr/share/texmf-texlive/fonts/truetype"
#my_env['TEXINPUTS'] = "/etc/texmf/texmf.d:/etc/texmf/texmf.cnf"
#my_env['TFMFONTS'] = "/etc/texmf/texmf.d"
my_env["TEXMFMAIN"]="/usr/share/texmf"
my_env["TEXMFDIST"]="/usr/share/texmf-texlive"
my_env["TEXMFLOCAL"]="/usr/local/share/texmf"
my_env["TEXMFSYSVAR"]="/var/lib/texmf"
my_env["TEXMFVAR"]='/home/eugene/.texmf-var'
my_env['TEXMFCONFIG']='/home/eugene/.texmf-config'
my_env['TEXMFHOME']='/home/eugene/texmf'
my_env['VARTEXFONTS']='/tmp/texfonts'

call(['/usr/bin/pdflatex', '/tmp/request.tex'],stdout=PIPE, env=my_env, shell=False )


from pyPdf import  PdfFileReader

_pdf_req = PdfFileReader(file('/tmp/request.pdf', 'rb'))
''' 
f = open('/tmp/page', 'w')                         
f.write(str(float(_pdf_req.getPage(0).mediaBox[3]) * 0.0352777778))
'''

_height = float(_pdf_req.getPage(0).mediaBox[3]) * 0.0352777778
'''
_command = 'lp -o page-left=0 -o page-right=0 -o page-top=0 -o page-bottom=0 -o media=Custom.80x%s'%_height + 'mm ./latex_test_new.pdf'
call([_command])
'''


_command = 'media=Custom.80x%s'%_height + 'mm ./request.pdf'
args = ['lp', '-o', 'page-left=0', '-o', 'page-right=0', '-o', "page-top=0", '-o', "page-bottom=0", '-o', "page-top=0", '-o', _command]
Popen(args)


