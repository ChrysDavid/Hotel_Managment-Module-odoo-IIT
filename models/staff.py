from odoo import models, fields

class Staff(models.Model):
    _name = 'hotel.staff'
    _description = 'Staff'

    JOB_POSITION = [
        ('receptionist', 'Réceptionniste'),
        ('housekeeping', 'Ménage'),
        ('maintenance', 'Maintenance'),
        ('manager', 'Manager')
    ]

    name = fields.Char(string='Nom', required=True)
    job_position = fields.Selection(JOB_POSITION, string='Rôle', required=True)
    hire_date = fields.Date(string="Date d'embauche", required=True)
    phone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
    salary = fields.Float(string='Salaire', required=True)
    building_id = fields.Many2one('hotel.building', string='Building', required=True)
