// JavaScript source code
$(document).ready(function(){
    $(".readMoreButton").click(function(){
		//Remove the focus from the button 
		this.blur()
        var info = $(this).siblings(".overFlowClipped");
		var buttonText = $(this).children("p").children("span");
		if (info.css("overflow") == "hidden") {
			info.css({"overflow":"visible","height":"auto"});
			buttonText.text("Hide");
		}
		else {
			info.css({"overflow":"hidden","height":"200px"});
			buttonText.text("Read more");
		}
    });
});
