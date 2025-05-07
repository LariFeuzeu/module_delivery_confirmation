from odoo import fields, models, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    physical_delivery_ok = fields.Boolean('physical delivery')
    has_tracking = fields.Char(
        string='Has Tracking')  # This field was added for the development upgrade. It didn't exist during the build, causing an error in the logs.

    physical_delivery_state = fields.Selection(
        [('pending', 'Livraison en attente'),
         ('partial_delivery', 'Livraison partielle'),
         ('done', 'Livraison effectuée')],
        string="État de livraison physique",
        compute='_compute_delivery_state',
        store=True
    )

    def action_warehousekeeper_confirmation(self):
        # For each picking in the current object
        for picking in self:
            # Updates the picking to indicate that the physical delivery is confirmed
            picking.write({'physical_delivery_ok': True})

            # Loops through each move line of the picking object
            for move_line in picking.move_lines:
                # If the move line is associated with a sale order line
                if move_line.sale_line_id:
                    # Marks the sale order line as delivered
                    move_line.sale_line_id.write({'delivery_ok': True})

                    # Returns True after performing all updates
        return True

    def action_cancel_delivery_confirmation(self):
        # Annuler la livraison pour chaque picking
        for picking in self:
            # Réinitialise le champ physical_delivery_ok
            picking.write({'physical_delivery_ok': False})

            # Parcours des lignes de mouvement et réinitialise la ligne de commande de vente
            for move_line in picking.move_lines:
                if move_line.sale_line_id:
                    # Annule la livraison pour la ligne de commande de vente
                    move_line.sale_line_id.write({'delivery_ok': False})

    @api.depends('sale_id.physical_delivery_state')
    def _compute_delivery_state(self):
        for picking in self:
            if picking.sale_id:
                picking.physical_delivery_state = picking.sale_id.physical_delivery_state
            else:
                picking.physical_delivery_state = 'pending'

    def action_print_invoice(self):
        for record in self:

            invoice = self.env['account.invoice'].search([('picking_id', '=', record.id)], limit=1)
            if not invoice:
                raise UserError("Aucune facture associée à ce picking")
            return self.env.ref('account.account_invoices').report_action(invoice)
