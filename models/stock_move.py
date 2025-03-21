from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    has_move_lines = fields.Boolean(
        string='has move lines')  # ici nous avons ajouter has_moves-lines a cause d'une erreur lors de l'affichage de la vue
