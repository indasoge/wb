 #-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Partner(models.Model):
    _inherit="res.partner"

    is_nave_crew = fields.Boolean(string='Es tripulante?',default=False)
    
    crew_category = fields.Selection(string='Categoria',

                                     selection=[('capitan','Capitán'),
                                                ('piloto','Piloto'),
                                                ('primerof','Primer Oficial'),
                                                ('segundoof','Segundo Oficial'),
                                                ('navegante','Navegante'),
                                                ('tecnicoMec','Técnico Mecánico'),
                                                ('tecnicoEle','Técnico Electrónico'),
                                                ('tecnicoComp','Técnico Computación'),
                                                ('tecnicoComun','Técnico Comunicaciones'),
                                                ('tripulante','Tripulante Básico')],
                                     copy=False, default='tripulante')
    
    mision_ids = fields.Many2many(comodel_name='exploracion.mision',
                                string="Misiones")
    
    number_missions = fields.Integer(string='Número de Misiones',default=0)
    
    



    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

