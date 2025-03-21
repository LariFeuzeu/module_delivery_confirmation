from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    physical_delivery_state = fields.Selection(
        [('pending', 'Livraison en attente'),
         ('partial_delivery', 'Livraison partielle'),
         ('done', 'Livraison effectuée')],
        string="État de livraison physique",
        compute='_compute_physical_delivery',
        store=True
    )

    @api.depends('order_line.qty_delivered', 'order_line.product_uom_qty', 'order_line.delivery_ok')
    def _compute_physical_delivery(self):

        for order in self:
            if all(line.delivery_ok and line.qty_delivered == line.product_uom_qty for line in order.order_line):
                order.physical_delivery_state = 'done'
            elif any(line.delivery_ok and line.qty_delivered < line.product_uom_qty for line in order.order_line):
                # Si au moins une ligne est partiellement livrée
                order.physical_delivery_state = 'partial_delivery'
            else:
                order.physical_delivery_state = 'pending'
