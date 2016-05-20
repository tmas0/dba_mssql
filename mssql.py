# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import print_function
import sys
import optparse

try:
    import pymssql
except ImportError, e:
    print (e)
    sys.exit(2)


def main(argv):
    p = optparse.OptionParser(conflict_handler="resolve", description="SQL Server management tool.")

    p.add_option('-H', '--host', action='store', type='string', dest='host', default=None, help='The hostname you want to connect to')
    p.add_option('-P', '--port', action='store', type='int', dest='port', default=1433, help='The SQL Server port is running on')
    p.add_option('-u', '--user', action='store', type='string', dest='user', default=None, help='The username you want to login as')
    p.add_option('-p', '--pass', action='store', type='string', dest='passwd', default=None, help='The password you want to use for that user')
    p.add_option('-d', '--database', action='store', dest='database', default=None, help='The database')
    p.add_option('-A', '--action', dest='action', default='show', help='You can choice: show or compact.')

    options, arguments = p.parse_args()

    host = options.host
    port = options.port
    user = options.user
    passwd = options.passwd
    database = options.database
    action = options.action

    err, con = mssql_connect(host, port, user, passwd, database)

    if err != 0:
        return err


def mssql_connect(host=None, port=None, user=None, passwd=None, database="tempdb"):
    ''' SQL Server connect '''
    try:
        conn = pymssql.connect(server, user, password, database)
    except Exception, e:
        return exit_with_general_critical(e), None
    return 0, conn


def exit_with_general_critical(e):
    if isinstance(e, SystemExit):
        return e
    else:
        print ("General SQL Server Error:", e)
    return 2