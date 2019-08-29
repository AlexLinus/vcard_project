$(document).ready(function () {
    $('#contact-form').on('submit',function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success : function (response) {
                if (response.status == 0){
                    // changing captcha image
                    $('.captcha').attr('src', response.new_cptch_image);
                    $('#id_captcha_0').val(response.new_cptch_key);
                    $('.form_errors').html(' Проверьте правильность введенных символов с картинки!');
                } else {
                    $('.form_errors').empty();
                    $('.form_success').html('Сообщение успешно отправлено!');
                    let new_comment = `<li><div class="row"><div class="col-md-10 col-sm-10 col-xs-9 comment-content"><div class="name">${response.new_comment_author_name}</div><span class="date">${response.new_comment_pub_date}</span><div id="comment-${response.new_comment_id}"><p>${ response.new_comment_body }</p></div><button class="get_quote" data-comment-id="comment-${ response.new_comment_id }"><i class="fa fa-reply" aria-hidden="true"></i>Цитировать</button></div></div></li>`;

                    $('#id_message').val('');
                    $('#id_captcha_1').val('');
                    $('.captcha').attr('src', response.new_cptch_image);
                    $('#id_captcha_0').val(response.new_cptch_key);
                    setTimeout(function() {
                        $('.form_success').empty();
                    }, 5000);
                };
            }
        }) //end ajax block
    })
});