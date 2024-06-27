from odoo.exceptions import ValidationError
from odoo import models, fields, api

class Payment(models.Model):
    _name = 'hotel.payment'
    _description = 'Payment'

    reference = fields.Char(string='Payment Reference', required=True)
    client_id = fields.Many2one('hotel.client', string='Client', required=True)
    invoice_id = fields.Many2one('hotel.invoice', string='Invoice', required=True, ondelete='cascade')
    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    method = fields.Selection([
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer')
    ], string='Payment Method', required=True)

    @api.constrains('invoice_id')
    def _check_invoice(self):
        for record in self:
            if not record.invoice_id:
                raise ValidationError("Invoice is required for payment.")
