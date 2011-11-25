function World(){
	var floor = new Image();
	floor.src = "stages.png";
	var sky = new Image();
	sky.src = "sky.png";
	this.draw = function(){
		var j = translations%10;
		screen.drawImage(sky,(100*j + (Math.floor(translations/10) *2000) ), 0, 1000, 640);
		screen.drawImage(sky, (100*(j+10) + (Math.floor(translations/10)*2000)), 0, 1000, 640);
		var i = 0;
		while(i<4){
			screen.drawImage(floor,0,0,200,640, 200*i,0,200,640);
			i++;
		}
		screen.drawImage(floor,200,0,200,640, 800,0,200,640);
	}
	this.getHeight = function(x){
		if(x<4){
			return 600;
		}else{
			return 300;
		}
	}
}



