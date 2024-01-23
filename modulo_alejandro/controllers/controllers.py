# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloAlejandro(http.Controller):
#     @http.route('/modulo_alejandro/modulo_alejandro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_alejandro/modulo_alejandro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_alejandro.listing', {
#             'root': '/modulo_alejandro/modulo_alejandro',
#             'objects': http.request.env['modulo_alejandro.modulo_alejandro'].search([]),
#         })

#     @http.route('/modulo_alejandro/modulo_alejandro/objects/<model("modulo_alejandro.modulo_alejandro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_alejandro.object', {
#             'object': obj
#         })
