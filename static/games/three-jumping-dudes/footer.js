controller = new Controller();
world = new World();
document.onkeydown=function(e){
	switch(e.keyCode){
		case 9:
			controller.change(-1);
			break;
		case 32:
			controller.attack();
			break;
		case 38:
			controller.jump();
			break;
		case 37:
			controller.left(true);
			break;
		case 39:
			controller.right(true);
			break;
		case 49:
			controller.change(0);
			break;
		case 50:
			controller.change(1);
			break;
		case 51:
			controller.change(2);
			break;
	}	
}
document.onkeyup=function(e){
	switch(e.keyCode){
		case 37:
			controller.left(false);
			break;
		case 39:
			controller.right(false);
			break;
	}
}
function run(){
	if( (green.x + red.x + blue.x) > 1200+600*translations){
		translations ++;
		screen.translate(-200, 0);
	}
	screen.clearRect(200*translations,0,800,640);
	world.draw();
	green.compute();
	red.compute();
	blue.compute();
	green.draw();
	red.draw();
	blue.draw();
}
setInterval(run, 20);