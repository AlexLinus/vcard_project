$(document).ready(function () {
    $('.get_quote').on('click', function (){
        let comment_id = $(this).attr('data-comment-id');
        $('#id_comment_body').val('<blockquote>' + $('#' + comment_id).text().trim().slice(0, 250) + '</blockquote>');
    });
});