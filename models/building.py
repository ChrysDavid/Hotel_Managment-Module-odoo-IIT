from odoo import models, fields
from odoo import models, fields

class Building(models.Model):
    _name = 'hotel.building'
    _description = 'Building'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    number_of_floors = fields.Integer(string='Number of Floors')
    rooms = fields.One2many('hotel.room', 'building_id', string='Rooms')
    spaces = fields.One2many('hotel.space', 'building_id', string='Spaces')
    staff = fields.One2many('hotel.staff', 'building_id', string='Staff')
    amenities = fields.Many2many('hotel.amenity', string='Amenities')
    # reservations = fields.One2many('hotel.reservation', 'building_id', string='Reservations')
