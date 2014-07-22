/**
 * Created by kremerdesign on 7/21/14.
 */





$.ajax({
        url: '/all_pokemon',
        type: "GET",
        success: function(data) {
            console.log(data);
        }
    });

