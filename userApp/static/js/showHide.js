$(document).ready(function() {
    $('#showCreateWeek').click(function() {
        $('#hideCreateWeek').animate( {
            width: 'toggle'
        })
    })
    $('#showCreateDay').click(function() {
        $('#hideCreateDay').animate( {
            width: 'toggle'
        })
    })
})