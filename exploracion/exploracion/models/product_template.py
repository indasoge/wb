# -*- coding:utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    
    is_ticket = fields.Boolean(string='Producto para vuelo de viajes espaciales comerciales',
                               help = 'Seleccione esta casilla para que sea un producto para vuelos espaciales',
                               default=False)
    
    