// JavaScript source code
function readMoreFunction() {
    var info = document.getElementById("readMore");
	var buttonText = document.getElementById("readMoreButton").firstChild.firstChild.firstChild;
    if (info.style.display == "none") {
        info.style.display = "block";
		buttonText.data = "Hide";
    } else {
        info.style.display = "none";
		buttonText.data = "Read more";
    }
}
