#!/usr/bin/env python

''' This is a the stop script which cleans the cache and kills all running processes.
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
