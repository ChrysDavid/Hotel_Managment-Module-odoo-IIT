odoo.define('hotel_management.reservation', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ReservationForm = publicWidget.Widget.extend({
        selector: '.hotel_reservation_page',
        events: {
            'change #building_id': '_onBuildingChange',
        },

        _onBuildingChange: function (ev) {
            var buildingId = $(ev.currentTarget).val();
            $('#room_id option').each(function () {
                var $option = $(this);
                if ($option.data('building') == buildingId) {
                    $option.show();
                } else {
                    $option.hide();
                }
            });
            $('#room_id').val('');
        },
    });

    return publicWidget.registry.ReservationForm;
});
