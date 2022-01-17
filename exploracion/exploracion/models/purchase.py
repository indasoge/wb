# -*- coding utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    mision_id = fields.Many2one(comodel_name='exploracion.mision',
                                 string = 'Viaje espacial',
                                 ondelete='set null')
    
