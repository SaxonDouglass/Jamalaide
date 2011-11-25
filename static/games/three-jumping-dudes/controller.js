function Controller(){
	this.player = 0; //0: green, 1: red, 2: blue
	this.leftVal = false;
	this.rightVal = false;
	//green.control(true);
	//red.control(false);
	
	this.change = function(i){
		if(i>=0){
			this.player = i;
		}else{
			this.player += 1;
		}
		this.player = this.player%3;
		
		if( this.player == 0 ){
			green.control = true;
		}else{
			green.control = false;
		}
		
		if( this.player == 1){
			red.control = true; 	
		}else {
			red.control = false;
		}
		
		if( this.player == 2 ){
			blue.control = true;
		}else{
			blue.control = false;
		}
	}
	this.left = function(bool){
		this.leftVal = bool;
		if(this.rightVal != bool){
			this.setDir(-1);
		}else{
			this.setDir(0);
		}
	}
	this.right = function(bool){
		this.rightVal = bool;
		if(this.leftVal != bool){
			this.setDir(1);
		}else{
			this.setDir(0);
		}
	}
	
	this.setDir = function(i){
		switch(this.player){
		case 0:
			green.setDir(i);
			break;
		case 1:
			red.setDir(i);
			break;
		case 2:
			blue.setDir(i);
			break;
		}
	}
	
	this.jump = function(){
		switch(this.player){
		case 0:
			green.jump();
			break;
		case 1:
			red.jump();
			break;
		case 2:
			blue.jump();
			break;
		}
	}
	
	this.attack = function(){
		switch(this.player){
		case 0:
			green.attack();
			break;
		case 1:
			red.attack();
			break;
		case 2:
			blue.attack();
			break;
		}
	}
}