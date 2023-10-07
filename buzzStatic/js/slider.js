var slider=document.getElementById("mood");
var emoji=document.getElementById("emoji");
var emoticons=["mood_bad", "sentiment_very_dissatisfied", 
    "sentiment_satisfied","sentiment_satisfied_alt",
    "sentiment_very_satisfied"
	];
slider.oninput=function(){
    emoji.innerHTML=emoticons[slider.value];
}