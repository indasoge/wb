 #-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Mision(models.Model):
    _name = 'exploracion.mision'
    _description = 'Mision Espacial'

    name=fields.Char(string='Identifier', required=True)
    description =fields.Text(string='Especifica los detalles de una misión espacial')
    
    origen = fields.Selection(string='Origen',
                             selection=[('tierra','Tierra')],
                             copy=False, default='tierra')
    
    destino = fields.Selection(string='Destino',
                             selection=[('tierra','Tierra'),
                                        ('sol','Sol'),
                                        ('mercurio','Mercurio'),
                                        ('venus','Venus'),
                                        ('luna','Luna'),
                                        ('marte','Marte'),
                                        ('jupiter','Júpiter'),
                                        ('saturno','Saturno'),
                                        ('urano','Urano'),
                                        ('neptuno','Neptuno'),
                                        ('pluton','Plutón')],
                             copy=False, default='luna')
    
    fecha_lanzamiento  = fields.Date(string='Fecha de Lanzamiento', required=True)
    fecha_retorno      = fields.Date(string='Fecha de Retorno')
    
    nave_id = fields.Many2one(comodel_name='exploracion.nave', string='Nave',
                             ondelete='cascade',
                             required = True)
    
    fligth_price = fields.Float(string = "Precio vuelo comercial")
    
    captain_id = fields.Many2one(comodel_name='res.partner', string ='Capitán',
                                 ondelete='cascade',
                                 required=True,
                                 domain="['&',('is_company','=', False), '&',('is_nave_crew','=',True),('crew_category','=','capitan')]"
                                )
    
    crew_ids = fields.Many2many(comodel_name='res.partner', 
                               string='Tripulantes',
                               domain="[('is_company','=',False),('is_nave_crew','=',True)]")
    
    
    
    active = fields.Boolean(string='Active', required=True, default=True)
    
    @api.onchange('captain_id')
    def _add_captain_to_crews(self):
        for record in self:
            curr_obj = self.env['exploracion.mision']
            if self.crew_ids:
                new_crew = [member.id for member in self.crew_ids if member.crew_category != self.captain_id.crew_category]
                new_crew.append(self.captain_id.id)
                #escribimos la nueva lista de tripulantes
                self.crew_ids = [(6,0,new_crew)] 
            else:
                self.crew_ids = self.captain_id

    @api.constrains('crew_ids')
    def _check_if_a_captain(self):
        for record in self:
            captains = [member for member in self.crew_ids if member.crew_category == 'capitan']
            if len(captains) == 0:
                raise ValidationError("Debe haber al menos un capitan en la tripulación")
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

