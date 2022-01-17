# -*- coding: utf-8 -*-
# from odoo import http


# class Exploracion(http.Controller):
#     @http.route('/exploracion/exploracion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exploracion/exploracion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exploracion.listing', {
#             'root': '/exploracion/exploracion',
#             'objects': http.request.env['exploracion.exploracion'].search([]),
#         })

#     @http.route('/exploracion/exploracion/objects/<model("exploracion.exploracion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exploracion.object', {
#             'object': obj
#         })
