from odoo import models, fields, api

class Room(models.Model):
    _name = 'hotel.room'
    _description = 'Room'

    name = fields.Char(string='Name', required=True)
    room_number = fields.Char(string='Room Number', readonly=True, default=lambda self: self._get_next_room_number())
    building_id = fields.Many2one('hotel.building', string='Building', required=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved')
    ], string='Status', default='available')
    ability = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string='Ability')
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string='Room Type')
    price = fields.Float(string='Price per Night')
    amenities = fields.Many2many('hotel.amenity', string='Amenities')
    image_ids = fields.One2many('hotel.room.image', 'room_id', string='Images')

    @api.model
    def _get_next_room_number(self):
        return self.env['ir.sequence'].next_by_code('hotel.room') or '0000'

    @api.model
    def create(self, vals):
        if 'room_number' not in vals or not vals['room_number']:
            vals['room_number'] = self._get_next_room_number()
        return super(Room, self).create(vals)

class RoomImage(models.Model):
    _name = 'hotel.room.image'
    _description = 'Room Image'

    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    image = fields.Binary(string='Image')
    description = fields.Char(string='Description')
