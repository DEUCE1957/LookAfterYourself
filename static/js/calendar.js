// JavaScript source code
function readMoreFunction() {
    //Get the element to be hidden or displayed
    var info = document.getElementById("readMore");
    //Get the text inside the button
	var buttonText = document.getElementById("readMoreButton").firstChild.firstChild.firstChild;
	//If it is not shown, show it and change the button text
    if (info.style.display == "none") {
        info.style.display = "block";
		buttonText.data = "Hide";
    } else {
        //If the text is visible, hide it

        info.style.display = "none";
		buttonText.data = "Read more";
    }
}
