	$("#formid").submit(function(e) {

		$("#formdiv").hide();
		$("#resultdiv").show();
		resetResult();

		e.preventDefault();
	});

	$("resetResult").click(function() {
		$("#formdiv").show();
		$("#resultdiv").hide();
	});

	$(document).ready(function() {
		$("#resultdiv").hide();
	});

	function resetResult() {
		$("#result").innerHTML = "Processing....";
	}