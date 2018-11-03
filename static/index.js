function setUp($question) {
    let $like = $question.find('.js-like');
    let $dislike = $question.find('.js-dislike');
    let $rating = $question.find('.js-rating');
    $like.on('click', function() {
        $.ajax({
            'url': 'https://yandex.ru/suggest/suggest-ya.cgi',
            'data': { 'part':  $question.data('telegram') },
            xhrFields: {
                withCredentials: true
            },
        }).done(function(resp) {
            alert('DONE');
            if (resp['status'] == 'ok') {
                let n = $rating.data('rating');
                n += 1;
                $rating.data('rating', n);
                $rating.text(n);
            }
            else if (resp.status == 'fail') {
                alert(resp['error']);
            }
        }).error(function(resp) {
            alert('ERR');
            alert(500);
        });
        return false;
    });
}

$(document).ready(function() {
    let $questions = $('.js-question');
    $questions.each(function() {
        let $question = $(this);
        setUp($question);
    });
});

$(function() {
    let cid = window.location.search;
    if (!cid) {
        return
    }
    cid = cid.substr(1);
    let ws_conn = new WebSocket("ws://127.0.0.1:8888/listen/?cid=" + cid);
    ws_conn.onopen = function() {
        alert('CONNECTED');
    };
    ws_conn.onmessage = function(evt) {
        alert(evt.data);
    };
});
