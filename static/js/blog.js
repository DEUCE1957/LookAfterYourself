// JavaScript source code
$(document).ready(function(){
    //Execute if a read more button is clicked
    $(".readMoreButton").click(function(){
		//Remove the focus from the button
		this.blur()
		//Get the blog text
        var info = $(this).siblings(".overFlowClipped");
        //Get the button text
		var buttonText = $(this).children("p").children("span");
		if (info.css("overflow") == "hidden") {
		    //If the overflow is hidden, show it and change the text of the button
			info.css({"overflow":"visible","height":"auto"});
			buttonText.text("Hide");
		}
		else {
		    //Similarly, if it is visible, hide it and change the text
			info.css({"overflow":"hidden","height":"200px"});
			buttonText.text("Read more");
		}
    });
});
