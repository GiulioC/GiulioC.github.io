document.getElementById("lavoro1").addEventListener("click", function(){manageLavori(1);});
document.getElementById("lavoro2").addEventListener("click", function(){manageLavori(2);});
document.getElementById("lavoro3").addEventListener("click", function(){manageLavori(3);});
document.getElementById("lavoro4").addEventListener("click", function(){manageLavori(4);});
document.getElementById("lavoro5").addEventListener("click", function(){manageLavori(5);});
document.getElementById("lavoro6").addEventListener("click", function(){manageLavori(6);});

var lastDiv = null

function manageLavori(num) {
	var divname = "#foto-lavoro-"+String(num)

	res = $('.foto-lavori').is(":visible")

	if ($(divname).is(":visible") == false) {
		changeStyle(num, true)
		$(".foto-lavori").hide()
		if (res == true) {
			changeStyle(lastDiv,false)
			lastDiv=String(num)
			$(divname).fadeIn()
			if ($(divname).visible(true) == false){
				$(document).scrollTop( $(divname).offset().top );
			}
		}
		else {
			$(divname).slideDown(function(){
				lastDiv = String(num)
				if ($(divname).visible(true) == false){
					$(document).scrollTop( $(divname).offset().top );
				}
			})
		}
	}
	else {
		$(".foto-lavori").slideUp(function(){changeStyle(num, false)})
	}
}

function changeStyle(divnum, bool){
	divID = "#lavoro"+String(divnum)
	if (bool){
		$(divID).css("opacity","0.5")
	}
	else {
		$(divID).css("opacity","")
	}
}

function showCaptions(){
	const language = document.URL.match(/\/([a-z]{2})\/photo/)[1]
	const hideLang = language === 'it' ? 'en' : 'it';
	$(`.desc-${hideLang}`).remove()
}
showCaptions();