# -*- encoding: utf-8 -*-

{
    'name': 'Scoop Partner',
    'version': '1.0',
    'author': 'AFRICA PERFORMANCES',
    'category': 'Customer Relationship Management',
	'license': 'AGPL-3',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
Ce module dédié aux sociétés cooperatives pour la gestion de leurs partenaires commerciaux
""",
    'depends': ['base', 'crm','sale_stock', 'account_accountant', 'partner_person',],
    'data': ['partner_view.xml',],
    'active': False,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: