from odoo import models, fields

class EmpProjet(models.Model):
    _name = 'empprojet'
    _description = 'Assignation des Employés à un Projet'

    employee_id = fields.Many2one('hr.employee', string="Employé", required=True)
    projet_id = fields.Many2one('project.project', string="Projet", required=True)

    #personnalized fields
    date_debut = fields.Date(string="Date de Début")
    date_fin = fields.Date(string="Date de Fin")
    total_heures = fields.Float(string="Total Heures", required=True)
