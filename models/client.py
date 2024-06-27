from odoo import models, fields

class Client(models.Model):
    _name = 'hotel.client'
    _description = 'Client'

    client_id = fields.Char(string='Client ID', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('hotel.client'))
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    invoices = fields.One2many('hotel.invoice', 'client_id', string='Invoices')
    history_reservations = fields.One2many('hotel.reservation', 'client_id', string='Reservations')
    preferences = fields.Selection([('smoking', 'Smoking'), ('non_smoking', 'Non Smoking')], string='Preference')
