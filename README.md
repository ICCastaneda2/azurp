What is this system:
Firstly, please be aware that this is a basic skeleton system which can be improve
either on the server side and on the client side.
However, what have been written so far can show how the system can improve
and what are the qulafications of the developers.
Also, the streaming is a mechanism which the developers have never used, and
have a little experience with generators,
so a curve of learing wad added to the time of the project.
Saying this, the following is a trial to follow the standard README.md style.

The system downloads infinite primes number allow the user to stop the process
and can show the current active downloads.

API
@app.route('/')   - the root sending the main index.html page
@app.route('/get_primes', methods=["GET"]) - downloads infinte primes numbers
@app.route('/finish_primes', methods=["GET"]) - finish the downloads
@app.route('/dashboard', methods=["GET"]) - show the current activities on one line in a circle 
                                            in 5 sec interval for each ip which is downloading.
  remarks:
  This is very base: we can add the following:
     1.show all activities in a in rows of the table, instead of wraping one one row in the table.
     2.Currently using a sample of a constant built in of list of dict of the activities.
       The activities can create and update by the flask server, deleting activities
       which ended and added new activities.
     3.The activities are pulled by the client on an interval of 5 sec. We can add a field
       to define the interval and a button to stop the dashboard show.
     4.There are 2 ways to show an on going activities of the server on an html page.
       1. One by pulling, which is used in this program and
       2. a websocket connection between the client and the server,
          which has not be develop in this case.
   

Motivation

To use streaming using generators

Installation

Clone the system from GitHub and follow the instruction to run it in the scripts folder

API Reference

See the above explanations

Tests

Tests / Mock system has not been created as it was not part of the project,
however tests and debug were done using PyCharm and print statements for the server side
and chrome built_in debugger and console.log() on the client side.


Contributors

This is a small project and done by me

Packages, 

  Packages on the server side
  import math
  from flask import Flask, request, Response
  from flask import jsonify, send_file

  On the client side "CDN" of jQuery, jQuery-UI, bootstrap and css.

General remarks:
  1. logging, argParse and configparser, can be added to have more user friendly control
     on the system.
  2. More conrol also can achieved thru enahancing the html pages.


