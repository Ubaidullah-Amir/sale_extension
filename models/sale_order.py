from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    my_name = fields.Char(string="My Name")