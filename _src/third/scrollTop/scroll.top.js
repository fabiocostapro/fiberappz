$(document).ready(function () {

    var largura_tela = $(window).width();
    if (largura_tela > 700) {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('.scroll-top').fadeIn();
            } else {
                $('.scroll-top').fadeOut();
            }
        });
        $('.scroll-top').click(function () {
            $("html, body").animate({
                scrollTop: 0
            }, 400);
            return false;
        });
    }
    
});