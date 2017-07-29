$(function() {
    console.log(top.location.pathname);

    $("#get-olts").on("click", ".olt-item-list", function() {
        var lorem = $(this).html();
        $("#olt-selected").html(lorem);
        $("#test-connection").css({"display": "block"});
        $("#test-connection .test-connection-loader").css({"display": "inline-block"});
        $("#test-connection .test-connection-success").css({"display": "none"});
        $("#test-connection .test-connection-error").css({"display": "none"});
        $.ajax({
            url: "/ssh-request/test-connection",
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
                console.log(response);
                $("#test-connection .test-connection-loader").css({"display": "none"});
                if(response == "True") {
                    $("#test-connection .test-connection-success").css({"display": "inline-block"});
                } else {
                    $("#test-connection .test-connection-error").css({"display": "inline-block"});
                }
            },
            error: function(error) {
                console.log(error);
            },
        });
    });

    $("#LOREMIPSUM").on("click", ".FOOBAR", function() {
        $.ajax({
            url: "/ssh-request/list-onts",
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
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
    });        

    $(".table").on("click", ".btn-cancel", function() {
        $(".authorize").css({"color": ""});
        $(this).parents("tr").remove();
    });

    $(".table").on("click", ".authorize", function() {
        if($(this).parents("tr").siblings(".authorize-confirm").length) {
            return false;
        }
        var Sn = ($(this).parent().siblings(".sn").html());
        var FSP = ($(this).parent().siblings(".fsp").html());
        var F = (FSP.slice(0, 1));
        var S = (FSP.slice(2, 3));
        var P = (FSP.slice(4, 5));
        var VendorId = ($(this).parent().siblings(".vendorid").html());
        var Description = ($(this).parent().siblings(".description").find("input").val());
        var Vlan = ($(this).parent().siblings(".vlan").find("input").val());
        if(VendorId == "LQDE") {
            var scriptType = "ont-lineprofile-id 3 ont-srvprofile-id 3";
        } else {
            var scriptType = "ont-lineprofile-id 1 ont-srvprofile-id 1";
        }
        var auth_sn = "<p class='authorize-sn'><strong>SN: </strong><span>" + Sn + "</span></p>";
        var auth_f = "<p class='authorize-f'><strong>F: </strong><span>" + F + "</span></p>";
        var auth_s = "<p class='authorize-s'><strong>S: </strong><span>" + S + "</span></p>";
        var auth_p = "<p class='authorize-p'><strong>P: </strong><span>" + P + "</span></p>";
        var auth_vendorid = "<p class='authorize-vendorid'><strong>VendorID: </strong><span>" + VendorId + "</span></p>";
        var auth_description = "<p class='authorize-description'><strong>Description: </strong><span>" + Description + "</span></p>";
        var auth_vlan = "<p class='authorize-vlan'><strong>VLAN: </strong><span>" + Vlan + "</span></p>";
        var auth_scripttype = "<p class='authorize-scripttype'><strong>Script: </strong><span>" + scriptType + "</span></p>";
        $("<tr class='authorize-confirm'><td colspan='7'>" + auth_sn + auth_f + auth_s + auth_p + auth_vendorid + '<br />' + auth_description + auth_vlan + '<br />' + auth_scripttype + "<a class='btn-cancel btn btn-default btn-s pull-right'>Cancel</a><a class='btn-confirm btn btn-default btn-p pull-right'><span class='loader'><i class='fa fa-refresh fa-spin'></i></span> Confirm</a></td></tr>").insertAfter($(this).parents("tr"));
        $(".alert").css({"display": "none"})
        $(".authorize").css({"color": "#ddd"});
    });

    $(".table").on("click", ".btn-confirm", function() {
        var sn = ($(this).siblings(".authorize-sn").find("span").html());
        var f = ($(this).siblings(".authorize-f").find("span").html());
        var s = ($(this).siblings(".authorize-s").find("span").html());
        var p = ($(this).siblings(".authorize-p").find("span").html());
        var vendorId = ($(this).siblings(".authorize-vendorid").find("span").html());
        var description = ($(this).siblings(".authorize-description").find("span").html());
        var vlan = ($(this).siblings(".authorize-vlan").find("span").html());
        if(vendorId == "LQDE") {
            var scriptType = "ont-lineprofile-id 3 ont-srvprofile-id 3";
            var gemPort = "37";
        } else {
            var scriptType = "ont-lineprofile-id 1 ont-srvprofile-id 1";
            var gemPort = "1";
        }
        $("i.fa", this).css({"display": "inline-block"});
        $("#alert-authorize").css({"display": "none"})
        $.ajax({
            url: "/ssh-request/authorize?sn=" + sn + "&f=" + f + "&s=" + s + "&p=" + p + "&vendorId=" + vendorId + "&description=" + description + "&vlan=" + vlan + "&scriptType=" + scriptType + "&gemPort=" + gemPort,
            type: "POST",
            success: function(response) {
                var response = JSON.parse(response);
                $(".authorize-confirm").remove();
                $(".authorize").css({"color": ""});
                if($.inArray("error", response) !== -1) {
                    $("#alert-authorize-error").css({"display": "block"});
                } else {
                    $("#alert-authorize-success").css({"display": "block"});
                }
            },
            error: function(error) {
                console.log(error);
            },
        });
    });

});
