from odoo import models, fields

class CustomProduit(models.Model):
    _inherit = 'product.product'

    stock_disponible = fields.Float(string="Stock Disponible", required=True)
    prix = fields.Float(string="Prix")
    categorie = fields.Char(string="Catégorie")

    def reduire_stock(self, quantite):
        if self.stock_disponible >= quantite:
            self.stock_disponible -= quantite
        else:
            raise ValueError("Stock insuffisant pour cette opération.")
