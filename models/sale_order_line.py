from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    delivery_ok = fields.Boolean(string="Livraison ok")

