"use strict";

$(document).ready(() => {
    $.post('YOUR_ENDPOINT_HERE')
    .done(visitor_counter => {
        $('#visits').text(visitor_counter);
    })
    .fail(e => {
        console.log('Error');
        console.log(e);
    });
});