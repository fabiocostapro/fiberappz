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
                    $("#ssh-request").append("<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td class='fsp'>" + value[2] + "/" + value[3] + "/" + value[4] + "</td><td>" + value[5] + "</td><td><div class='input-group'><input class='form-control' type='text' /></div></td><td></td><td><a id='authorize'>View & Authorize</></td></tr>");
                });
                $("#ssh-request").css({"display": "table-row-group"});
                $("#main-loader").css({"display": "none"});
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    $(".table").on("click", "#authorize", function() {
        var FSP = ($(this).parent().siblings(".fsp").html());
        var F = (FSP.slice(0, 1));
        var S = (FSP.slice(2, 3));
        var P = (FSP.slice(4, 5));

        $.ajax({
            url: "/ssh-request/authorize?F=" + F + "&S=" + S + "&P=" + P,
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

});
