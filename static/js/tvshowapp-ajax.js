$(document).ready(function() {
    $('#like_btn').click(function() {
    var shshowIdVar;
    shshowIdVar = $(this).attr('data-showid');
    $.get('/TVShowApp/like-show/',
    {'show_id': shshowIdVar},
    function(data) {
    $('#like_count').html("Likes: " + data);
    $('#like_btn').hide();
    })
    });
    });
    