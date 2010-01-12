#!/bin/bash

sudo cp -rf cgi-bin/*  /usr/lib/cgi-bin/ #in ubuntu
sudo cp css/peter.css /var/www/css/ #depends on the path in header.html
sudo cp -rf muse/ ~/.emacs.d/ #depends on what in .emacs
