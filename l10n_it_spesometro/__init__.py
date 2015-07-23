# -*- coding: utf-8 -*-
##############################################################################
#    
#    Author: Alessandro Camilli (a.camilli@yahoo.it)
#    Copyright (C) 2014
#    Associazione OpenERP Italia (<http://www.openerp-italia.org>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import spesometro
import wizard
import logging
import os.path
_logger = logging.getLogger(__name__)
try:
    from l10n_it_bbone import wizard
    _logger.info("Comunicazione Polivalente standard")
    l10n_it_base="l10n_it_bbone"
except ImportError:
    _logger.info("Comunicazione Polivalente compatibile con l10n_it_base")
    l10n_it_base="l10n_it_base"
mfx_ffn=os.path.abspath(os.path.join(__file__, '..', '__openerp__.py'))
fd=open(mfx_ffn,'rb')
s=fd.read().replace('l10n_it_base',l10n_it_base).replace('l10n_it_bbone',l10n_it_base)
fd.close() 
fd=open(mfx_ffn,'wb')
fd.write(s)
fd.close()