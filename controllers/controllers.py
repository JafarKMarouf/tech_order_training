# -*- coding: utf-8 -*-
# from odoo import http


# class TechOrderTraining(http.Controller):
#     @http.route('/tech_order_training/tech_order_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_order_training/tech_order_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_order_training.listing', {
#             'root': '/tech_order_training/tech_order_training',
#             'objects': http.request.env['tech_order_training.tech_order_training'].search([]),
#         })

#     @http.route('/tech_order_training/tech_order_training/objects/<model("tech_order_training.tech_order_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_order_training.object', {
#             'object': obj
#         })

