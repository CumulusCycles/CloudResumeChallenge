"use strict";

$(document).ready(() => {
    $.post('YOUR_ENDPOIONT')
    .done(visitor_counter => {
        console.log(visitor_counter);
        $('#visits').text(visitor_counter);
    })
    .fail(e => {
        console.log('Error');
        console.log(e);
    });
});