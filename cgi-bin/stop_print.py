#!/usr/bin/env python

import lib_print
import cgi, os, cgitb
cgitb.enable()

from lib_print import *

# if a logfile exists, we are currently printing, so stop it
file = os.path.join(cache_folder, log_lock_file)
if os.path.exists(file):
   # Check if this request really comes from our form and not only the url is called
   form = cgi.FieldStorage()
   if form.getvalue('confirm'):
      clean_cache()
      # TODO: also stop the send.py script and make sure everything is clean and done!
      redirect_index()
   else:
      redirect_index()
else:
   redirect_index()
