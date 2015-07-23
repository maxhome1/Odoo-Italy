# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) SHS-AV s.r.l. (<http://www.zeroincombenze.it>)
#    All Rights Reserved
#
#    Written by Alessando Camilli (alessandrocamilli@openforce.it).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

"""
    Simple Trace & Debug module V0.3
    Write into specific tracelog located at /var/log/openerp/oe_trace.log
    Messages are recorded by tndb.wlog
"""

# import pdb
import datetime
import inspect
from datetime import datetime


# use:
# from tndb.tndb import tndb
# ...
# tndb.wlog('test' ...)
class tndb():

    @staticmethod
    def wlog(*args):
        txt = datetime.now().strftime("%Y-%m-%d %H:%M:%S\t")
        sp = ''
        for arg in args:
            try:
                if isinstance(arg, unicode):
                    txt = txt + sp + arg.encode('utf-8')
                elif isinstance(arg, str):
                    txt = txt + sp + arg
                else:
                    txt = txt + sp + str(arg).encode('utf-8')
            except:
                x = unichr(0x3b1) + unichr(0x3b2) + unichr(0x3b3)
                txt = txt + sp + x.encode('utf-8')
            sp = ' '
        txt = txt + "\n"
        log_of = open("/var/log/openerp/oe_trace.log", "a")
        log_of.write(txt)
        log_of.close()

    @staticmethod
    def wstamp(*args):
        m = len(inspect.stack())
        if m>5:
            m = 5
        m -= 1
        # txt = datetime.now().strftime("%Y-%m-%d %H:%M:%S\t")
        sep = ""
        txt = "\n"
        for i in range(m, 0, -1):
            x = inspect.stack()[i][1].rfind(".")
            n = inspect.stack()[i][1][0:x]
            if n[-3:] == "osv":
                n = "osv"
            elif n[-3:] == "orm":
                n = "orm"
            txt = txt + sep + n
            txt = txt + ":" + str(inspect.stack()[i][2])
            txt = txt + " " + inspect.stack()[i][3] + "()" + "\n"
            sep += "  "
        # txt = txt + "|\n"
        # log_of = open("/var/log/openerp/oe_trace.log", "a")
        # log_of.write(txt)
        # log_of.close()
        tndb.wlog(txt, args)
