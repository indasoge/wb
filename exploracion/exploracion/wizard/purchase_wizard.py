# -*- coding:utf-8 -*-

from odoo import models, fields, api

class PurchaseWizard(models.TransientModel):
    _name = "exploracion.purchase.wizard"
    _description = "Wizard rápido para compras para pagar a los tripulantes"
    
    def _default_mision(self):
        return self.env['exploracion.mision'].browse(self._context.get('active_id'))
    
    mision_id = fields.Many2one(comodel_name="exploracion.mision",
                                string="Mision",
                                required=True,
                                default=_default_mision)
    
    fare = fields.Float(string="Pago a tripulantes",
                        required=True)
    
    mision_crew_ids = fields.Many2many(comodel_name='res.partner',
                                       string = 'Tripulantes de la mision',
                                       related = 'mision_id.crew_ids',
                                       help='Tripulantes de la mision')
    
    purchase_crew_ids = fields.Many2many(comodel_name='res.partner',
                                        string = 'Tripulantes en la orden de compra')
    
    
    def create_purchase_orders(self):
        
        mision_product_id = self.env['product.product'].search([('is_ticket','=',True)], limit=1)
        
        if mision_product_id:
            for tripulante in self.purchase_crew_ids:
                order_id = self.env['purchase.order'].create({
                        'partner_id':tripulante.id,
                        'mision_id': self.mision_id.id,
                        'order_line':[(0,0,{'product_id': mision_product_id.id, 'price_unit':self.fare})]
                })
    
    
    
    
