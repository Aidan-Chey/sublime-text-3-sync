#!/usr/bin/env python
#coding: utf8
#################################### IMPORTS ###################################

# Std Libs
import os

# Sublime Libs
import sublime
import sublime_plugin

################################################################################

class MakeReadOnly(sublime_plugin.EventListener):
    def on_activated(self, view):
        fn = view.file_name()
        if not fn: return
        view.set_read_only(not os.access(fn, os.W_OK))

################################################################################