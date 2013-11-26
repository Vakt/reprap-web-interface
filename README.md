reprap-web-interface
====================

A tiny web interface for pushing gcode files to a reprap printer and starting the print-job.

INSTALL
-------
Dependencies: webserver (eg: lighttpd), python 2.7
Enable cgi in you webserver configs and copy all files into you web server direcotry (e.g: /var/www/).
Further you might need to adjust the owner of the files and execution rights (e.g: chown *www-data:www-data *: chmod a+x cgi-bin;)

USAGE
-----
Call the index.html file from any web-browser, upload a *.gcode file made for your reprap printer and press "Start". As long as a print-job is running, you will be redirected to running.html where you cal also stop the current job.

TODO
----
The stop-script is not finished yet, I still need to implement killing the actual process and sending a reset gcode file to the printer. Furhter a natural end of the print-job is not yet recogniced.

