$(function() {
    console.log(top.location.pathname);

    if(top.location.pathname === "/control-panel"){
        $(window).on("load", SshRequest);
        function SshRequest() {
            $.ajax({
                url: "/ssh-request/list-onts",
                type: "POST",
                success: function(response) {
                    var response = JSON.parse(response);
                    console.log(response);
                    if($.inArray("error", response) !== -1) {
                        $("#alert-list-onts").css({"display": "block"})
                        $("#main-loader").css({"display": "none"});
                    } else {
                        $.each(response, function(index, value) {
                            $("#ssh-request").append("<tr><td>" + value[0] + "</td><td class='sn'>" + value[1] + "</td><td class='fsp'>" + value[2] + "/" + value[3] + "/" + value[4] + "</td><td class='vendorid'>" + value[5] + "</td><td class='description'><div class='input-group'><input class='form-control' type='text' /></div></td><td class='vlan'><div class='input-group'><input class='form-control' type='text' /></div></td><td><a class='authorize'>Authorize</a></td></tr>");

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
    }

    $(".table").on("click", ".authorize", function() {
        var Sn = ($(this).parent().siblings(".sn").html());
        var FSP = ($(this).parent().siblings(".fsp").html());
        var F = (FSP.slice(0, 1));
        var S = (FSP.slice(2, 3));
        var P = (FSP.slice(4, 5));
        var VendorId = ($(this).parent().siblings(".vendorid").html());
        var Description = ($(this).parent().siblings(".description").find("input").val());
        var Vlan = ($(this).parent().siblings(".vlan").find("input").val());
        if(VendorId == "LQDE") {
            var scriptType = "ont-srvprofile-id 3";
        } else {
            var scriptType = "ont-srvprofile-id 1";
        }

        var scriptLine1 = "<strong>SN: </strong>" + Sn;
        var scriptLine2 = "<strong>F/S/P: </strong>" + F + "/" + S + "/" + P;
        var scriptLine3 = "<strong>VendorID: </strong>" + VendorId;
        var scriptLine4 = "<strong>Description: </strong>" + Description;
        var scriptLine5 = "<strong>VLAN: </strong>" + Vlan;
        var scriptLine6 = "<strong>Script: </strong>" + scriptType;
        console.log("VendorID= " + VendorId);

        $("<tr><td colspan='5'></td><td colspan='3' class='authorize-confirm'>" + scriptLine1 + "<br />" + scriptLine2 + "<br />" + scriptLine3 + "<br />" + scriptLine4 + "<br />" + scriptLine5 + "<br />" + scriptLine6 + "<a id='btn-cancel' class='btn btn-default btn-s pull-right'>Cancel</a><a id='btn-confirm' class='btn btn-default btn-p pull-right'>Confirm</a></td></tr>").insertAfter($(this).parents("tr"));

        $("i.fa", this).css({"display": "inline-block"});
        $(".authorize").click(false);
        $("#alert-authorize").css({"display": "none"})
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
                    $("#alert-authorize").css({"display": "block"})
                    $("#main-loader").css({"display": "none"});                 
                } else {
                    $(".authorize i.fa").css({"display": "none"});
                    $(".authorize").css({"display": "inline-block"});
                }
            },
            error: function(error) {
                console.log(error);
            },
        });
    });

});
