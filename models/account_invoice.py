from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'  # On hérite de account.invoice dans Odoo 11

    physical_delivery_state = fields.Selection(
        [('pending', 'Livraison en attente'),
         ('partial_delivery', 'Livraison partielle'),
         ('done', 'Livraison effectuée')],
        string="État de la livraison physique",
        compute='_compute_physical_delivery_state',
        store=True
    )

    @api.depends('invoice_line_ids.sale_line_ids.delivery_ok', 'picking_id')
    def _compute_physical_delivery_state(self):
        for invoice in self:
            if invoice.type == 'out_invoice' and invoice.picking_id:
                order = invoice.picking_id.move_lines[0].sale_line_id.order_id
                invoice.physical_delivery_state = order.physical_delivery_state
            elif invoice.type == 'out_invoice' and invoice.picking_id.state == 'done':
                invoice.physical_delivery_state = 'pending'
            else:
                invoice.physical_delivery_state = False

