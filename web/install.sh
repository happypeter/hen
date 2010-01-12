#!/bin/bash

sudo cp -rf cgi-bin/*  /usr/lib/cgi-bin/ 
#this is the place to put cgi scripts in ubuntu

sudo cp css/peter.css /var/www/css/ #depends on the path in header.html

sudo cp -rf muse/ ~/.emacs.d/ #depends on what in .emacs

sudo rm /var/www/*.html
# now I can go to emacs and publish the new web with C-c-p
