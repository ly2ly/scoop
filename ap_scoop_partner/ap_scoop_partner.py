# -*- coding: utf-8 -*-
# © <2017> <Africa Performances>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp
from openerp import tools, api
from openerp.osv import fields, osv, orm
from openerp.osv.expression import get_unaccent_wrapper

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import email_re, email_split

from lxml import etree
import math
import pytz
import urlparse

from datetime import datetime
from operator import itemgetter




#
class scoop_section(osv.osv):
    """ Section of Scoop """

    _name = "scoop.section"
    _description = "Scoop Partner section"

    _columns = {
            'name': fields.char('Section', size=50, help="Section farmer"),
            'active': fields.boolean('Active', help="Actif"),
#set default values to active
            }


class scoop_area(osv.osv):
    """ area of Scoop """

    _name = "scoop.area"
    _description = "Scoop Delegue area"

    _columns = {
            'name': fields.char('Area', size=50, help="Area delegue"),
            'active': fields.boolean('Active', help="Actif"),
#set default values to active
            }

#
class production_year(osv.osv):
    """ Production"""

    _name = "scoop.production"
    _description = "Scoop Partner production"

    _columns = {
            'name': fields.integer('Annee', help="Annee de production"),
            'qty': fields.boolean('Qty', help="Quantite produite"),
            'uom': fields.boolean('Unit', help="unit de mesure"),
            }

#
class scoop_partner(osv.osv):
    """ Partners of Scoop """

    _name = "res.partner"
    _inherit = "res.partner"

    _columns = {
            'is_certified': fields.boolean('Est certifie', help="Le planteur est il certifie?"),
            'is_farmer': fields.boolean('Est planteur', help="Le partenaire est il un planteur?"),
            'is_delegue': fields.boolean('Est delegue', help="Le partenaire est il un delegue?"),
            'code': fields.char('Code', size=50, help="Code planteur"),
            'section_id': fields.many2one('scoop.section', 'Section', help="Section planteur"),
            'area_id': fields.many2one('scoop.area', 'Area', help="Area delegue"),
            'date_integ': fields.date('Date Integration', help="Date d'intégration"),
            'date_inspect': fields.date('Date Inspection', help="Date d'inspection Interne"),
            'date_approb': fields.date('Date Approbation', help="Date d'approbation"),
            'nbre_plantation': fields.integer('Nombre de Plantations', help="Nombre de Plantations detenus par le planteur"),
            'sup_total': fields.float('Superficie totale (Hectare)', help="Superficie totale des plantations detenus par le planteur"),
            'sup_product': fields.float('Superficie Produit (Hectare)', help="Superficie totale du Produit detenus par le planteur"),
            'product_id': fields.many2one('product.product', 'produit', size=200, help="Produit"),
            'sup_jachere': fields.float('Superficie en Jachere (Hectare)', help="Superficie totale en jachere du planteur"),
            'sup_cult': fields.float('Superficie autres cultures (Hectare)', help="Superficie des autres cultures detenus par le planteur"),
            'sup_foret': fields.float('Superficie totale (Hectare)', help="Superficie totale des plantations detenus par le planteur"),
            'age_plant': fields.integer('Age plantation', help="Age des Plantations detenus par le planteur"),
            #'production_ids'
            }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
