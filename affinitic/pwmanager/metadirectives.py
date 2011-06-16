# -*- coding: utf-8 -*-
"""
affinitic.pwmanager

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
from zope.schema import TextLine, Bool
from zope.interface import Interface


class IPwdFileDirective(Interface):
    """
    Directive to register a password File
    """

    filename = TextLine(
        title=u"Name of the file containing the login/pass information",
        description=u"""This file needs to be created at the INSTANCE/var
        level.""",
        required=False,
        )

    name = TextLine(
        title=u"The unique name of the login/pass information",
        description=u"""""",
        required=True,
        )

    separator = TextLine(
        title=u"Separtor char which split the login with the password",
        description=u"",
        required=False)

    filepath = TextLine(
        title=u"Filename with its complete path",
        description=u"",
        required=False)

    required = Bool(
        title=u"Does the file needs to exists ?",
        description=u"",
        required=False)
