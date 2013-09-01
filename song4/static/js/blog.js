var submit_url = "/comment/submit/";

function submit_comment() {
	var content = $('textarea[name="content"]').val();
	var author_name = $('input[name="author_name"]').val();
	var author_email = $('input[name="author_email"]').val();
	var author_url = $('input[name="author_url"]').val();

	var data = $('#comment-box form').serializeArray();
	console.debug(data);

	$.post(submit_url, data);
}

$('#comment-box button').click(function(e) {
	e.preventDefault();
	submit_comment();
});
