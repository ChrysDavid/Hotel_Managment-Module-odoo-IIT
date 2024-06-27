from odoo import models, fields

class Invoice(models.Model):
    _name = 'hotel.invoice'
    _description = 'Invoice'

    number = fields.Char(string='Invoice Number', required=True)
    client_id = fields.Many2one('hotel.client', string='Client', required=True)
    date_create = fields.Date(string='Date', required=True)
    date_due = fields.Date(string='Due Date', required=True)
    reservations = fields.Many2many('hotel.reservation', string='Reservations')
    amount = fields.Float(string='Amount', required=True)
    state = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid')
    ], string='Status', default='draft')
    payment_ids = fields.One2many('hotel.payment', 'invoice_id', string='Payments')
