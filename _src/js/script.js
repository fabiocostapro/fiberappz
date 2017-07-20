$(function() {
    console.log("0");
    $(window).on("load", SshRequest);
    function SshRequest() {
        $.ajax({
            url: "/ssh-request/list-onts",
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
                console.log(response);
                if($.inArray("error", response) !== -1) {
                    $("#alert-request").css({"display": "block"})
                    $("#main-loader").css({"display": "none"});
                } else {
                    $.each(response, function(index, value) {
                        $("#ssh-request").append("<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td class='fsp'>" + value[2] + "/" + value[3] + "/" + value[4] + "</td><td>" + value[5] + "</td><td class='desc-form'><div class='input-group'><input class='form-control' type='text' /></div></td><td class='vlan-form'><div class='input-group'><input class='form-control' type='text' /></div></td><td><a class='authorize'><span class='loader'><i class='fa fa-refresh fa-spin'></i></span> View & Authorize</></td></tr>");
                    });
                    $("#ssh-request").css({"display": "table-row-group"});
                    $("#main-loader").css({"display": "none"});
                };
            },
            error: function(error) {
                console.log(error);
            },
        });
    };

    $(".table").on("click", ".authorize", function() {
        var FSP = ($(this).parent().siblings(".fsp").html());
        var F = (FSP.slice(0, 1));
        var S = (FSP.slice(2, 3));
        var P = (FSP.slice(4, 5));
        $("i.fa", this).css({"display": "inline-block"});
        $(".authorize").not(this).css({"display": "none"});
        $.ajax({
            url: "/ssh-request/authorize?F=" + F + "&S=" + S + "&P=" + P,
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
                console.log(response);
                if($.inArray("error", response) !== -1) {
                    console.log(response);
                    $(".authorize i.fa").css({"display": "none"});
                    $(".authorize").css({"display": "inline-block"});
                } else {
                    $("#alert-request").css({"display": "block"})
                    $("#main-loader").css({"display": "none"});                   
                }
            },
            error: function(error) {
                console.log(error);
            },
        });
    });

});
