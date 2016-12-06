#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

host = '127.0.0.1'

try:
    con = _mysql.connect(host, 'ubuntu', '', 'circle_test')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()
