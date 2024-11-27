from odoo import models, fields

class ProdProj(models.Model):
    _name = 'prodprojet'
    _description = 'Utilisation des Produits dans un Projet'

    produit_id = fields.Many2one('product.product', string="Produit", required=True)
    projet_id = fields.Many2one('project.project', string="Projet", required=True)
    
    date_achat = fields.Date(string="Date d'Achat")
    quantite = fields.Float(string="Quantité", required=True)
    prix_unitaire = fields.Float(string="Prix Unitaire", required=True)

    def calculer_cout_total(self):
        return self.quantite * self.prix_unitaire
