var editor, controls;
var c_hidden_left = -270;
var c_toggle_duration = 800;


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

	left = ($(document).width() - $('#title-indicator').width()) / 2;
	$('#title-indicator').css({'left': left + 'px'});
}

function run_editor() {
	editor = ace.edit("editor");
	editor.setHighlightActiveLine(false);	// Don't highlight the active line.
	editor.setShowPrintMargin(false);		// Don't show the print margin.
	editor.getSession().setMode("ace/mode/markdown");
	editor.getSession().setUseWrapMode(true);
}

function init_page() {
	$(document).ready(function() {
		controls = $('#controls');

		run_editor();
		make_editor_center();

		hide_controls();
		controls.mouseenter(show_controls);
		controls.mouseleave(hide_controls);
	});

	window.onresize = make_editor_center;
}
