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

$(document).ready(function() {
    $(document).on("click", "#approve_btn", function() {
        var shshowIdVar;
        shshowIdVar = $(this).attr('data-showid');
        $.get('/TVShowApp/approve-show/',
              {'show_id':shshowIdVar},
              function(data){
                  $('#'+shshowIdVar).hide();
              })
    })
});

$(document).ready(function() {
    $(document).on("click", "#delete_btn", function() {
        var shshowIdVar;
        shshowIdVar = $(this).attr('data-showid');
        $.get('/TVShowApp/deny-show/',
              {'show_id':shshowIdVar},
              function(data){
                  $('#'+shshowIdVar).hide();
              })
    })
});
    