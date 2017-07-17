$(function() {

    console.log("START");

    $(window).on("load", SshRequest);
    function SshRequest() {
        $.ajax({
            url: "/ssh-request/list-onts",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);

                $.each(response, function(index, value) {
                    $("#ssh-request").append("<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "/" + value[3] + "/" + value[4] + "</td><td>" + value[5] + "</td><td></td><td></td><td></td></tr>");
                });


                $("#ssh-request").css({"display": "table-row-group"});
                $("#main-loader").css({"display": "none"});
            },
            error: function(error) {
                console.log(error);
            }
        });
    } 

});
