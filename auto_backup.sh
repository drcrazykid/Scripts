#!/bin/bash

TIME='date +%b-%d-%y'
FILENAME=backup-scripts-$TIME.tar.gz
SRCDIR=/home/$(whoami)/Documents/python_scripts
DESDIR=/home/$(whoami)/Documents/script_backups
tar -cpzf $DESDIR/$FILENAME $SRCDIR
