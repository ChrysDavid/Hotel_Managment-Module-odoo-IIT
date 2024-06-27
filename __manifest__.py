{
    'name': 'Hotel Management',
    'version': '1.0',
    'category': 'Hotel',
    'summary': 'Hotel Management System',
    'description': """
    A module to manage hotels including buildings, rooms, amenities, clients, invoices, payments, staff, spaces, and planning.
    """,
    'author': 'Brou David',
    'depends': ['base', 'website'],
    'data': [
        'data/room_sequence.xml',
        'security/ir.model.access.csv',
        'views/building_views.xml',
        'views/room_views.xml',
        'views/amenity_views.xml',
        'views/client_views.xml',
        'views/invoice_views.xml',
        'views/payment_views.xml',
        'views/planning_views.xml',
        'views/reservation_views.xml',
        'views/staff_views.xml',
        'views/space_views.xml',
        'views/website_reservation_template.xml',
        'views/client_signup_views_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hotel_management/static/src/js/website_reservation.js',
        ],
    },
    'images': ['static/description/hotel.jpg'],
    'icon': 'static/description/icon.png',
    'installable': True,
    'application': True,
    'auto_install': False,
}
