#!/usr/bin/env python

''' This is a small library for the start and stop python script.
    Copyright (C) 2013  Stefan Hammer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import cgi, cgitb, os, subprocess
cgitb.enable()

# Variables
cache_folder = '../cache/'
log_lock_file = 'lock.log'

# Function definitions
def system_execute(command, path, out_file):
    params_list = command.split(' ') 
    file_path = os.path.join(path, out_file)
    f = open(file_path, "w")
    sp = subprocess.Popen(params_list, stdout=f, stderr=f)
    sp.wait()
    f.close()

def clean_cache():
    for a_file in os.listdir(cache_folder):
       file_path = os.path.join(cache_folder, a_file)
       try:
          os.unlink(file_path)
       except Exception, e:
          print e

def redirect_running():
   print "Location: /running.html"
   print

def redirect_index():
   print "Location: /index.html"
   print

def print_error(message):
   print """\
   Content-Type: text/html\n
   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN'
   'http://www.w3.org/TR/html4/strict.dtd'>
   <html>
   <head>
   <title>RepRap Printer</title>
   <meta http-equiv='content-type' content='text/html; charset=UTF-8'>
   <link rel='stylesheet' href='/style.css'>
   </head>
   <body>
   <h1><img src='/logo.svg' alt='RepRap' title='RepRap'></h1>
   <h2>Error...</h2>
   <p style='color:red;'>%s</p>
   <button onclick='window.history.back()'>Try again</button>
   <div id="footer">Copyright &copy; 2013 <a href="http://www.tbi.univie.ac.at">TBI Vienna</a>, <a href="http://www.gnu.org/licenses/">GPLv3.0</a></div>
   </body>
   </html>
   """ % (message,)
