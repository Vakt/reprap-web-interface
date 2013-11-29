#!/usr/bin/env python

''' This is the start script which calls send.py or redirects in case of errors
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
         
         system_execute('/usr/bin/python ../Printrun/printcore.py -v -s /dev/ttyUSB0 ' + cache_folder + fn, cache_folder, log_lock_file)
         redirect_running()
         
      # Print some Error Messages   
      else:
         print_error('No GCode file was uploaded. Please try again!')
   except Exception:
      redirect_index()
