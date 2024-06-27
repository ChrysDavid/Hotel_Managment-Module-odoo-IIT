from odoo import models, fields

class Amenity(models.Model):
    _name = 'hotel.amenity'
    _description = 'Amenity'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    type = fields.Selection([
        ('basic', 'Basic'),
        ('premium', 'Premium')
    ], string='Type')
    cost_amenity = fields.Integer(string='Additional Cost')
    image = fields.Binary(string='Image')  # Champ pour l'upload d'image
