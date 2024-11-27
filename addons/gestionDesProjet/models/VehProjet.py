from odoo import models, fields

class VehProjet(models.Model):
    _name = 'vehprojet'
    _description = 'Assignation des Véhicules à un Projet'

    vehicule_id = fields.Many2one('fleet.vehicle', string="Véhicule", required=True)
    projet_id = fields.Many2one('project.project', string="Projet", required=True)
    
    date_utilisation = fields.Date(string="Date d'Utilisation")
    cout = fields.Float(string="Coût", required=True)
