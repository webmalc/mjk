$(document).ready(function () {

    if (window.AjaxForm) {
        AjaxForm.Message.success = function () { };
    }

});
$(document).on('af_complete', function (event, response) {
    var form = response.form;
    if (response.success) {

        $('.modal__feedback').hide()
        $('.modal__kp').hide()
        $('.modal__feedback-success').show()
        setTimeout(() => {
            $('.modal__feedback-success').hide()
            $('body').attr('style', '')
        }, 5000);

     

    } else {

    }

});