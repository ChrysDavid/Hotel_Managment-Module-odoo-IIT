from odoo import http, fields
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class HotelWebsite(http.Controller):

    @http.route('/reservation/', type='http', auth="public", website=True)
    def hotel_reservation(self, **kwargs):
        buildings = request.env['hotel.building'].sudo().search([])
        rooms = request.env['hotel.room'].sudo().search([])
        clients = request.env['hotel.client'].sudo().search([])
        return request.render('hotel_management.hotel_reservation_page', {
            'buildings': buildings,
            'rooms': rooms,
            'clients': clients,
            'checkin_date': fields.Date.today(),
        })

    @http.route('/reservation/submit/', type='http', auth="public", website=True, methods=['POST'])
    def hotel_reservation_submit(self, **kwargs):
        client_id = kwargs.get('client_id')
        room_id = kwargs.get('room_id')
        checkin_date = kwargs.get('checkin_date')
        checkout_date = kwargs.get('checkout_date')

        if not client_id or not room_id or not checkin_date or not checkout_date:
            error_message = "Please fill in all required fields."
            return request.render('hotel_management.error_page', {'error': error_message})

        try:
            client_id = int(client_id)
            room_id = int(room_id)
        except ValueError:
            error_message = "Invalid client or room ID format."
            return request.render('hotel_management.error_page', {'error': error_message})

        try:
            reservation_vals = {
                'client_id': client_id,
                'room_id': room_id,
                'checkin_date': checkin_date,
                'checkout_date': checkout_date,
                'status': 'confirmed',
            }
            reservation = request.env['hotel.reservation'].sudo().create(reservation_vals)
            _logger.info('Reservation created successfully: %s', reservation)
        except Exception as e:
            error_message = f"Failed to create reservation: {e}"
            return request.render('hotel_management.error_page', {'error': error_message})

        return request.redirect('/reservation/thank_you/')

    @http.route('/signup', type='http', auth='public', website=True)
    def client_signup(self, **post):
        if post.get('name') and post.get('email') and post.get('phone'):
            Client = request.env['hotel.client']
            client_vals = {
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'address': post.get('address', ''),
            }
            client = Client.create(client_vals)
            return request.redirect('/thankyou')
        else:
            return request.render('hotel_management.client_signup_form')

    @http.route('/thankyou', type='http', auth='public', website=True)
    def client_signup_thankyou(self, **post):
        return request.render('hotel_management.client_signup_thankyou')
