# -*- coding: utf-8 -*-
"""
affinitic.pwmanager

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
import os
from zope.interface import implements
from affinitic.pwmanager.interfaces import IPasswordManager


class PasswordManager(object):
    """
    A password manager
    """
    implements(IPasswordManager)

    def __init__(self):
        self.name = ""
        self.username = None
        self.password = None

    def _getFile(self, filename, filepath):
        if filepath is None:
            var = os.environ.get('PASSWORD_DIR')
            if var is None:
                var = os.environ.get('CLIENT_HOME')
                if var is None:
                    raise "Can't find PASSWORD_DIR or CLIENT_HOME in your environment ... export it before execute this script"
                var = os.path.join(var, os.path.pardir)
                var = os.path.abspath(os.path.join(var, 'pass'))
            filepath = os.path.join(var, filename)
        try:
            fd = open(filepath, 'r')
        except:
            fd = None
        return fd

    def registerFromFile(self, filename, name, separator, filepath, required):
        fd = self._getFile(filename, filepath)
        if fd is None:
            if required == True:
                raise IOError("Can't open password file: %s %s" % (filepath, filename))
        else:
            data = fd.read()
            data.strip()
            if separator not in data:
                raise Exception("Can't find separator %s in password file %s %s" % (separator,
                                                                                    filepath,
                                                                                    filename))
            login, password = data.split(separator)
            self.register(name, login.strip(), password.strip())

    def register(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def getLoginPass(self):
        """
        return a tuple containing a login/password
        """
        return (self.username, self.password)

    def getLoginPassWithSeparator(self, separator):
        """
        return a string containing a login and a password separated by
        seperator
        """
        return '%s%s%s' % (self.username, separator, self.password)
