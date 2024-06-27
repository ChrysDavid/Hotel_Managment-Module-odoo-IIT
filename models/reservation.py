from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Reservation'

    reservation_number = fields.Char(string='Reference', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('hotel.reservation'))
    client_id = fields.Many2one('hotel.client', string='Client', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    checkin_date = fields.Date(string='Check-in Date', required=True)
    checkout_date = fields.Date(string='Check-out Date', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    building_id = fields.Many2one('hotel.building', string='Building', required=True)

    @api.onchange('building_id')
    def _onchange_building_id(self):
        self.room_id = False

    @api.model
    def create(self, vals):
        vals['reservation_number'] = self.env['ir.sequence'].next_by_code('hotel.reservation') or 'New'
        result = super(Reservation, self).create(vals)
        return result

    def action_confirm(self):
        for record in self:
            record.status = 'confirmed'

    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'
