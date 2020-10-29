$(document).ready(function () {
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 200) {
            $('.scroll-top').removeClass('not-visible');
        } else {
            $('.scroll-top').addClass('not-visible');
        }
        //console.log($(this).scrollTop());
    });
    $('.scroll-top').on('click', function (event) {
        $('html,body').animate({
            scrollTop: 0
        }, 1000);
    });
});