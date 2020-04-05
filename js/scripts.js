function onClick(){
	var text = document.getElementById("demo").innerHTML;
	if (text == 0){
		text = 1;
	}
	else{
		text = 0;
	}
	document.getElementById("demo").innerHTML = text;
}