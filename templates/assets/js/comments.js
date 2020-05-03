$(document).ready(function () {
    if ('comment_name' in localStorage && 'comment_email' in localStorage) {
        $('#id_author_name').val(localStorage.getItem('comment_name'));
        $('#id_author_email').val(localStorage.getItem('comment_email'));
    };

    $('.get_quote').on('click', function (){
        let comment_id = $(this).attr('data-comment-id');
        $('#id_comment_body').val('<blockquote>' + $('#' + comment_id).text().trim().slice(0, 250) + '</blockquote>');
    });

    $('#comment-form').on('submit', function (e) {
        e.preventDefault();
        let name = $('#id_author_name').val();
        let email = $('#id_author_email').val();
        localStorage.setItem('comment_name', name);
        localStorage.setItem('comment_email', email);

        let form = $('#comment-form');
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: $(this).serialize(),
            success : function (response) {
                if (response.status == 0){
                    let errors = response.form_errors;
                    // changing captcha image
                    $('.captcha').attr('src', response.new_cptch_image);
                    $('#id_captcha_0').val(response.new_cptch_key);
                    $('.form_errors').html(' Проверьте правильность введенных символов с картинки!');
                } else {
                    $('.form_errors').empty();
                    $('.form_success').html('Комментарий успешно добавлен!');
                    let new_comment = `<li><div class="row"><div class="col-md-10 col-sm-10 col-xs-9 comment-content"><div class="name">${response.new_comment_author_name}</div><span class="date">${response.new_comment_pub_date}</span><div id="comment-${response.new_comment_id}"><p>${ response.new_comment_body }</p></div><button class="get_quote" data-comment-id="comment-${ response.new_comment_id }"><i class="fa fa-reply" aria-hidden="true"></i>Цитировать</button></div></div></li>`;

                    if( $('#comments-list li').length >= 1 ){
                        $("#comments-list li:last").after(new_comment);
                    } else {
                        $("#comments-list").append(new_comment);
                    }
                    $('#id_comment_body').val('');
                    $('#id_captcha_1').val('');
                    $('.captcha').attr('src', response.new_cptch_image);
                    $('#id_captcha_0').val(response.new_cptch_key);
                    setTimeout(function() {
                        $('.form_success').empty();
                    }, 5000);
                };
            }
        })
    })
});