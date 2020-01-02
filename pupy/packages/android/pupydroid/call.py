#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: @bobsecq
#Contributor(s):

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from jnius import autoclass

def getCallDetails():
    '''
    '''
    calls = []
    Calls = autoclass('android.provider.CallLog$Calls')
    PythonActivity = autoclass('org.renpy.android.PythonService')
    cursor = PythonActivity.mService.getContentResolver().query(Calls.CONTENT_URI, None, None, None, Calls.DATE+" DESC")
    callsCount = cursor.getCount()
    if callsCount > 0:
        while cursor.moveToNext():
            phNum = cursor.getString(cursor.getColumnIndex(Calls.NUMBER))
            callTypeCode = cursor.getString(cursor.getColumnIndex(Calls.TYPE))
            callDate = cursor.getString(cursor.getColumnIndex(Calls.DATE))
            callDuration = cursor.getString(cursor.getColumnIndex(Calls.DURATION))
            calls.append({'phNum':phNum,'callTypeC':callTypeCode,'callDate':callDate, 'callDuration':callDuration})
    cursor.close()
    return calls
