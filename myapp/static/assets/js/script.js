$(function() {
    console.log("try2");

    $.ajaxSetup({
        headers: {
            'X-CSRF-TOKEN': $('meta[name="_token"]').attr('content')
        }
    });


    $("#ls").click(function(){
        $.ajax({
            url: "/ssh-request/ls",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                $("#output").html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $("#uptime").click(function(){
        $.ajax({
            url: "/ssh-request/uptime",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                $("#output").html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });


});
