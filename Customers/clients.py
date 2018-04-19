
# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
from openerp.tools.translate import _
import calendar
import datetime

class Hrclients(models.Model):
    _name = "hr.clients"
    _description = "clients"
    def get_first_day(self):
        today = datetime.datetime.today()
        return datetime.date(today.year, today.month, 1).strftime('%Y-%m-%d')

    def get_last_day(self):
        today = datetime.datetime.today()
        __day__ = calendar.monthrange(today.year, today.month)[1]
        return datetime.date(today.year, today.month, __day__).strftime('%Y-%m-%d')
   
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('waiting', "En attente"),
        ('ended', 'Validé'),
    ],
        "Eat des ventes ",
        select=True,
        readonly=True,
        default='draft')
    periode = fields.Date('Date' )
    partner_id = fields.Many2one('res.partner', string='Clients', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always')
    date_du = fields.Date('Date du', required=True,default=get_first_day)
    date_au = fields.Date('Date au ', required=True,default=get_last_day)
    comiss_ids = fields.One2many('hr.ligne.ventes', 'Commission_id', string='Lignes des ventes')


class Hrligneventes(models.Model):
    _name = "hr.ligne.ventes"
    _description = "lignes des ventes"


    @api.depends('poid', 'prix_uni')
    def _compute_amount(self):
        for line in self:
            line.montant = line.poid * line.prix_uni 
    

    

   
    @api.depends ('poid','taux_com')
    def _compute_com(self):
        for line in self:        
            line.Commission = line.poid * line.taux_com

    

    @api.depends ('montant','Commission')
    def _compute_total(self):
        for line in self:
            line.total = line.montant + line.Commission

    periode = fields.Date('Date' )
    nombre_sac = fields.Integer ("Nombre de Sacs")
    poid = fields.Float (string="Poids")
    prix_uni = fields.Float(string="Prix Unitaire")
    taux_com = fields.Float(string="Taux Commission")
    montant = fields.Float(compute=_compute_amount, string='Montant')
    Commission=fields.Float(compute=_compute_com,string="Commission")
    total = fields.Float(compute=_compute_total, string="Total")
    Commission_id = fields.Many2one('hr.clients','Reference to parent')
	

    #subtotal_nombre_sac = fields.Float(string='Sous-total', compute='_amount_all', store=True)
    #subtotal_poid = fields.Float(string='Sous-total', compute='_amount_all', store=True)
    #subtotal_prix_uni = fields.Float(string='Sous-total', compute='_amount_all', store=True)
    #subtotal_montant = fields.Float(string='Sous-total', compute='_amount_all', store=True)
    #subtotal_totall = fields.Float(string='Sous-total', compute='_amount_all', store=True)
    #total = fields.Float(string='Total', compute='_amount_all', store=True)



    #@api.depends('Commission_id')
    #def _amount_all(self):
    #    for Hrligneventes in self:
    #        Hrligneventes.subtotal_nombre_sac = sum([line.nombre_sac for line in Hrligneventes.Commission_id])
    #        Hrligneventes.subtotal_poid = sum([line.poid for line in Hrligneventes.Commission_id])
    #        Hrligneventes.subtotal_prix_uni = sum([line.prix_uni for line in Hrligneventes.Commission_id])
    #        Hrligneventes.subtotal_montant = sum([line.montant for line in Hrligneventes.Commission_id])
    #        Hrligneventes.subtotal_total = sum([line.total for line in Hrligneventes.Commission_id])

            