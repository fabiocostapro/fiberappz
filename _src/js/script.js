$(function() {

console.log("START");

// $(window).on("load", SshRequest);
function SshRequest() {
    $.ajax({
        url: "/ssh-request/ls",
        data: $("form").serialize(),
        type: "POST",
        success: function(response) {
            console.log(response);
            $("#ssh-request").html(response);
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
} 

$("#switch").click(function(){
    $("#ssh-request").toggle();
    $("#main-loader").toggle();
    console.log("SWITCH")
});  

});
