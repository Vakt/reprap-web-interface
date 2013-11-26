#!/usr/bin/env python

import cgi, os, subprocess
import cgitb
import lib_print
cgitb.enable()

from lib_print import *

# if a logfile exists, we are currently printing, just redirect to running.html
if os.path.exists(os.path.join(cache_folder, log_lock_file)):
   redirect_running()

# Do all the magic: file upload, start printing,...   
else:
   try:
      form = cgi.FieldStorage()
      # A nested FieldStorage instance holds the file
      fileitem = form['filename']
    
      # Test if the file was uploaded
      if fileitem.filename:
         
         # first delete all previous uploads and logs
         clean_cache()
         
         # strip leading path from file name to avoid directory traversal attacks
         fn = os.path.basename(fileitem.filename)
         open(cache_folder + fn, 'wb').write(fileitem.file.read())
         # message = 'The file "' + fn + '" was uploaded successfully'
         
         system_execute('/usr/bin/python send.py -v -b 115200 -n ' + cache_folder + fn, cache_folder, log_lock_file)
         redirect_running()
         
      # Print some Error Messages   
      else:
         print_error('No GCode file was uploaded. Please try again!')
   except Exception:
      redirect_index()
