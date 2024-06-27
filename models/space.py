from odoo import models, fields

class Space(models.Model):
    _name = 'hotel.space'
    _description = 'Space'

    SPACE_TYPE = [
        ('conference_room', 'Salle de conférence'),
        ('pool', 'Piscine'),
        ('spa', 'Spa'),
        ('restaurant', 'Restaurant'),
        ('gym', 'Salle de sport'),
        ('meeting_room', 'Salle de réunion')
    ]

    AVAILABILITY_STATUS = [
        ('available', 'Disponible'),
        ('not_available', 'Non disponible')
    ]

    name = fields.Char(string='Nom de l\'espace', required=True)
    type_space = fields.Selection(SPACE_TYPE, string="Type d'espace")
    capacity = fields.Integer(string="Capacité maximale de l'espace")
    availability = fields.Selection(AVAILABILITY_STATUS, string="Statut de disponibilité de l'espace")
    rate = fields.Integer(string="Tarif d'utilisation de l'espace")
    building_id = fields.Many2one('hotel.building', string='Building', required=True)
