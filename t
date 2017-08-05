#!/bin/bash
dir=`dirname $0`
/home/jiri/dev/anaconda3/bin/python3 $dir/t.py "`zenity --text='' --entry`"
