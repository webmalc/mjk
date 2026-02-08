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
            if (window.history.replaceState) {
                const url = new URL(window.location.href)
                url.searchParams.delete('success')
                window.history.replaceState({}, document.title, url.toString())
            }
        }, 5000);

     

    } else {

    }

});