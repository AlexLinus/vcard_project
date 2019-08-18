$(document).ready(function () {
    if ('comment_name' in localStorage && 'comment_email' in localStorage) {
        $('#id_author_name').val(localStorage.getItem('comment_name'));
        $('#id_author_email').val(localStorage.getItem('comment_email'));
    };

    $('.get_quote').on('click', function (){
        let comment_id = $(this).attr('data-comment-id');
        $('#id_comment_body').val('<blockquote>' + $('#' + comment_id).text().trim().slice(0, 250) + '</blockquote>');
    });

    $('#add-comment').on('click', function () {
        let name = $('#id_author_name').val();
        let email = $('#id_author_email').val();
        localStorage.setItem('comment_name', name);
        localStorage.setItem('comment_email', email);
    })
});