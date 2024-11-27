from odoo import models, fields

class CustomProjet(models.Model):
    _inherit = 'project.project'

    date_debut = fields.Date(string="Date de Début")
    date_fin = fields.Date(string="Date de Fin")
    etat = fields.Selection([
        ('en_cours', "En cours"),
        ('termine', "Terminé"),
        ('annule', "Annulé")
    ], string="État", default='en_cours')
    
    total_cout = fields.Float(string="Coût Total", compute="_compute_total_cout", store=True)

    # def _compute_total_cout(self):
    #     for projet in self:
    #         cout_employes = sum(emp.cout_jh * emppro.total_heures for emppro in projet.empprojet_ids for emp in emppro.employee_id)
    #         cout_vehicules = sum(vp.cout for vp in projet.vehprojet_ids)
    #         cout_produits = sum(pp.prix_unitaire * pp.quantite for pp in projet.prodprojet_ids)
    #         projet.total_cout = cout_employes + cout_vehicules + cout_produits

    def _compute_total_cout(self):
      for projet in self:
        projet.total_cout = 0  # Test sans empprojet

    # Nouvelle méthode pour le bouton "Terminer"
    def action_done(self):
        for projet in self:
            if projet.etat != 'termine':  # Si l'état n'est pas déjà 'Terminé'
                projet.etat = 'termine'
            else:
                raise UserError("Le projet est déjà terminé.")


    def ajouter_employe(self, employe, total_heures):
        self.env['empprojet'].create({
            'projet_id': self.id,
            'employee_id': employe.id,
            'total_heures': total_heures,
        })
