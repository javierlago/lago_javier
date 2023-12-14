# -*- coding: utf-8 -*-
# from odoo import http


# class LagoJavier(http.Controller):
#     @http.route('/lago_javier/lago_javier', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lago_javier/lago_javier/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lago_javier.listing', {
#             'root': '/lago_javier/lago_javier',
#             'objects': http.request.env['lago_javier.lago_javier'].search([]),
#         })

#     @http.route('/lago_javier/lago_javier/objects/<model("lago_javier.lago_javier"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lago_javier.object', {
#             'object': obj
#         })
