from odoo import models, fields

class CustomEmployee(models.Model):
    _inherit = ['hr.employee']
    _description = "employée de l'entreprise"

    cout_jh = fields.Float(string="Coût Journalier par Heure", required=True)
    fonction = fields.Selection([
        ('ouvrier', "Ouvrier"),
        ('contremaitre', "Contremaître"),
        ('architecte', "Architecte")
    ], string="Fonction")
    
    def calculer_cout_total(self, nb_heures):
        return self.cout_jh * nb_heures
