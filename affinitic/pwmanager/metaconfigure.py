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


def pwdFile(_context, name, filename=None, separator=':', filepath=None, required=True):
    pwManager = PasswordManager()
    pwManager.registerFromFile(filename, name, separator, filepath, required)
    provideUtility(pwManager, IPasswordManager, name)
