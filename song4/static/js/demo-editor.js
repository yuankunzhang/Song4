var editor, controls;
var c_hidden_left = -250;		// 控制栏隐藏的距离
var c_toggle_duration = 800;	// 控制栏淡入/淡出时间
var s_interval = 60000;			// 自动保存时间间隔


function save_post() {
	$('#save-indicator').fadeIn().delay(2000).fadeOut();
}

function show_controls() {
	if (controls.position().left == c_hidden_left) {
		controls.animate({
			left: 0,
			opacity: 1
		}, c_toggle_duration, 'swing');
	}

	if (editor) {
		editor.blur();
	}
}

function hide_controls() {
	if (controls.position().left == 0) {
		controls.animate({
			left: c_hidden_left,
			opacity: 0.3
		}, c_toggle_duration, 'swing');
	}

	if (editor) {
		editor.focus();
	}
}

function make_editor_center() {
	var left = ($(document).width() - $('#editor').width()) / 2;
	$('#editor').css({'left': left + 'px'});
	$('#save-indicator').css({'left': left + 'px'});

	left = ($(document).width() - $('#title-indicator').width()) / 2;
	$('#title-indicator').css({'left': left + 'px'});
}

function resize_editor() {
		var newHeight = editor.getSession().getScreenLength() *
			editor.renderer.lineHeight +
			editor.renderer.scrollBar.getWidth();
		$('#editor').height(newHeight.toString() + 'px');
		editor.resize();
}

function run_editor(content) {
	editor = ace.edit("editor");
	editor.setHighlightActiveLine(false);	// Don't highlight the active line.
	if (content) {
		editor.getSession().setValue(content);
		resize_editor();
	}

	editor.setShowPrintMargin(false);		// Don't show the print margin.
	editor.getSession().setMode("ace/mode/markdown");
	editor.getSession().setUseWrapMode(true);
	editor.getSession().on('change', resize_editor);
}

function init_page(content) {
	$(document).ready(function() {
		controls = $('#controls');

		run_editor(content);
		make_editor_center();

		hide_controls();
		controls.mouseenter(show_controls);
		controls.mouseleave(hide_controls);

		setInterval(save_post, s_interval);
	});

	window.onresize = make_editor_center;
}
