from odoo import models, fields

class Planning(models.Model):
    _name = 'hotel.planning'
    _description = 'Planning'

    name = fields.Char(string="Event or Reservation Name", required=True)
    staff_id = fields.Many2one('hotel.staff', string='Staff', required=True)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date', required=True)
    type_event = fields.Selection([
        ('meeting', 'Meeting'),
        ('conference', 'Conference'),
        ('event', 'Event')
    ], string="Event Type")
    participants = fields.Selection([
        ('small', 'Small (1-10)'),
        ('medium', 'Medium (11-50)'),
        ('large', 'Large (51+)')
    ], string="Participants List")
