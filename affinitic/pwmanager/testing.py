# -*- coding: utf-8 -*-
"""
affinitic.pwmanager

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

"""
from zope.component import provideUtility
from zope.interface import implements
from affinitic.pwmanager.interfaces import IPasswordManager
from affinitic.pwmanager.pwmanager import PasswordManager


def pwdFile(_context, name, filename=None, separator=':', filepath=None, required=True):
    pwManager = PasswordManagerTesting()
    provideUtility(pwManager, IPasswordManager, name)


class PasswordManagerTesting(PasswordManager):
    """
    A password manager
    """
    implements(IPasswordManager)

    def __init__(self):
        self.name = ""
        self.username = 'foo'
        self.password = 'foo'
