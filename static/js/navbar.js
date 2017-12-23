function navbar() {
	a = document.querySelector("#navbarToggle");
	b = document.querySelectorAll(".des");
	a.addEventListener("click", function() {
		for (let i=0; i<b.length; i++) {
			if (b[i].style.display == "none" || b[i].style.display == "")
				b[i].style.display = "block";
			else 
				b[i].style.display = "none";
		}
	});
}
navbar();