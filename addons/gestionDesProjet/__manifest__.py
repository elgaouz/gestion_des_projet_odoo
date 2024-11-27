{
    'name': 'Gestion de projets',
    'version': '1.0.0',
    'sequence': -100,
    'author': 'Imane El gaouz',
    'summary': 'Gestion de projets',
    'description': ' Projet qui a pour but de gerer les projets de construction',
    'depends': ['base','hr','fleet','project', 'product'],
  'data': [
    'views/projet_views.xml',
    'views/empprojet_views.xml',
    'views/vehprojet_views.xml',
    'views/prodprojet_views.xml',
    'views/produit_views.xml',
    'views/employe_views.xml',
    'views/vehicule_views.xml',
    'security/ir.model.access.csv',

],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}