 #-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Nave(models.Model):
    _name = 'exploracion.nave'
    _description = 'Nave Espacial'

    name=fields.Char(string='Identifier', required=True)
    description =fields.Text(string='Nombre usual')
    
    length = fields.Float(string='Length', required=True)
    width  = fields.Float(string='Width', required=True)
    heigth  = fields.Float(string='Heigth', required=True)
    
    fuel_type = fields.Selection(string='Fuel Type', required=True,
                                selection=[('solido','Sólido'),
                                           ('liquido','Líquido')],
                                copy=False,default='solido')
    
    ship_type = fields.Selection(string='Ship Type', required=True,
                                selection=[('comercial', 'Comercial'),
                                          ('carguero','Carguero'),
                                          ('naveCombate','Nave de combate')],
                                copy=False, default='carguero')
    
    cost_crew = fields.Float(string="Tarifa tripulación")
    
    crew_number = fields.Integer(string='Dotación', required=True)
    
    passanger_number = fields.Integer(string='Número de pasajeros', required=True)
    
    active = fields.Boolean(string='Active', required=True, default=True)
    
    mision_ids = fields.One2many(comodel_name='exploracion.mision',
                                inverse_name='nave_id',
                                string='Misiones')
    
    @api.constrains('length','width')
    def _check_width_length(self):
        for record in self:
            if record.width >= record.length:
                raise ValidationError("El ancho %s debe ser menor al largo %s" %(record.width,record.length))

    @api.constrains('crew_number')
    def _check_crew_number(self):
        for record in self:
            if record.crew_number < 3 and record.ship_type != 'naveCombate':
                raise ValidationError('La dotación de tripulación no puede se inferior a 3, valor introducido %s' % record.crew_number)
            if record.crew_number < 1 and record.ship_type == 'naveCombate':
                raise ValidationError('La dotación de tripulación no puede se inferior a 1, valor introducido %s' % record.crew_number)
                
    @api.onchange('ship_type')
    def _onchange_ship_type_fuel(self):
        for record in self:
            if record.ship_type == 'naveCombate':
                record.fuel_type = 'liquido'
            else:
                record.fuel_type = 'solido'


    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

