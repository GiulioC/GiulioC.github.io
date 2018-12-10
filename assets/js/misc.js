$('#foto-avatar').click(function(e) {
	console.log("Ciao !")
})

$('#all-skills-show').click(function(e) {
	$('#all-skills-show').hide()
		$('#all-skills').slideDown()
})

$('#all-skills-hide').click(function(e) {
	$('#all-skills').slideUp(function() {
		$('#all-skills-show').fadeIn()
	})
})
