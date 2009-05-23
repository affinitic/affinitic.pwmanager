# -*- coding: utf-8 -*-
"""
affinitic.pwmanager

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from zope.interface import Interface, Attribute


class IPasswordManager(Interface):
    """
    A password manager
    """

    name = Attribute('The unique name related to this login/pass')

    username = Attribute('The login')

    password = Attribute('The password')

    def register(name, username, password):
        """
        register a login/pass
        """

    def registerFromFile(filename, name, separator=':'):
        """
        register a login/pass from the content of a file
        """

    def getLoginPass():
        """
        return a tuple containing a login/password
        """

    def getLoginPassWithSeparator(separator):
        """
        return a string containing a login and a password separated by
        seperator
        """
