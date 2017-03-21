# -*- coding: utf-8 -*-

import os

class cmd_executer:

    def execute(self,cmd):
        print "Executing >> " + cmd
        b = os.system(cmd)
        print "return code = %d"%(b) + "\n"