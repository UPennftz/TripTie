// JavaScript/jQuery code
$(document).ready(function() {
    $('.like-btn').click(function() {
        var $button = $(this);
        var tripPlanId = $button.data('trip-plan-id');
        var likeCount = parseInt($button.siblings('.like-count').text());

        $.ajax({
            type: 'GET',
            url: '/like_trip_plan/' + tripPlanId + '/',
            success: function(response) {
                if (response.liked) {
                    likeCount++;
                    $button.addClass('liked'); // Add the 'liked' class to change button color
                } else {
                    likeCount--;
                    $button.removeClass('liked'); // Remove the 'liked' class
                }
                $button.siblings('.like-count').text(likeCount);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});