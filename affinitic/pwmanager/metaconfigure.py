# -*- coding: utf-8 -*-
"""
affinitic.pwmanager

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from affinitic.pwmanager.pwmanager import PasswordManager
from affinitic.pwmanager.interfaces import IPasswordManager
from zope.component import provideUtility


def pwdFile(_context, filename, name, separator=':'):
    pwManager = PasswordManager()
    pwManager.registerFromFile(filename, name, separator)
    provideUtility(pwManager, IPasswordManager, name)
