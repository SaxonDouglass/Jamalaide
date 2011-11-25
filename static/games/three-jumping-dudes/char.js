function Character(xIn, yIn, colour, selected){
	this.x = xIn;
	this.y = yIn;
	this.w = 48;
	this.h = 48;
	this.yVel = 0;
	this.xVel = 0;
	this.facing = 1;
	this.jumps = 0;
	this.control = selected;
	var move = false;
	var spriteRate = 5;
	var speed = 10;
	var acc = 1;
	var jumpCap = 2;
	var jumpPower = 18;
	var charSprite = new Image();
	charSprite.src=colour+"Sprite.png";
	var attackSprite = new Image();
	var wepH = 0;
	var wepW = 0;
	var wepDur = 0;
	var animState = 0;
	var animCount = 0;
	var swing = 0;
	var swingCount = 0;
	var id;
	
	switch(colour){
		case "green":
			this.h = 64;
			id = 0;
			speed = 10;
			jumpCap = 2;
			break;
		case "red":
			id = 1;
			speed = 10;
			jumpCap = 1;
			jumpPower = 15;
			attackSprite.src="hammerSprite.png";
			wepH = 64;
			wepW = 48;
			wepDur = 5;
			break;
		case "blue":
			this.h = 64;
			id = 2;
			speed = 10;
			jumpCap = 1;
			break;
		default:
			id = 0;
			break;
	}
	
	this.setDir = function(i){
		if(i){
			this.facing = i;
			this.move = true;
		}else{
			this.move = false;
		}
	}
	this.xCheck = function(){
		if(this.control == true){
			if(this.move){
				this.xVel = speed*this.facing;
			}else{
				this.xVel = 0;
			}
		}else{
			var targetX
			switch(id){
				case 0:
					targetX = blue.x;
					break;
				case 1:
					targetX = green.x;
					break;;
				case 2:
					targetX = red.x;
					break;
			}
			if((this.x-30) > (targetX)){
				this.xVel = -speed;
				this.facing = -1;
			}else if((this.x+30) < (targetX)){
				this.xVel = speed;
				this.facing = 1;
			}else{
				this.xVel = 0;
			}
		}
	}

	this.compute = function(){
		var groundHeight;
		var step;
		if(this.x%200 + this.xVel > 200){
			groundHeight = world.getHeight(Math.floor(this.x/200)+this.facing);
			step = true;
		}else{
			groundHeight = world.getHeight(Math.floor(this.x/200));
			step = false;
		}
		var altitude = groundHeight - this.y - this.h;
		if(altitude >  -(this.h)){
			if(altitude > 0){
				//Airborne
				this.yVel = this.yVel + acc;
				this.y = this.y + this.yVel;
				animState = 1;
			}else{
				//Walking
				this.xCheck();
				this.y = groundHeight-this.h;
				this.yVel = 0;
				this.jumps = jumpCap;
				if(this.xVel == 0){
					animState = 0;
				}else{
					animCount++;
					animState = 1+Math.floor((animCount/spriteRate)%4);
				}
			}
			this.x += this.xVel;
		}else{
			this.x -= this.xVel;
		}
		var targetY
		switch(id){
			case 0:
				targetY = blue.y;
				break;
			case 1:
				targetY = green.y;
				break;;
			case 2:
				targetY = red.y;
				break;
		}
		if(this.y-50>targetY && this.control != true){
			this.jump();
		}
	}
	
	this.draw = function(){
		if(this.facing != -1){
			if(swing > 0){
				screen.drawImage(attackSprite, wepW*(swing-1), wepH, wepW, wepH, this.x+16, this.y+this.h-wepH, wepW,wepH);
				swingCount++;
				if(swingCount>=(spriteRate/3)){
					swing--;
					swingCount = 0;
				}
			}
			screen.drawImage(charSprite, this.w*animState, this.h,this.w, this.h, this.x, this.y, this.w, this.h);
		}else{
			if(swing > 0){
				screen.drawImage(attackSprite, wepW*(wepDur - swing),0, wepW,wepH, this.x+this.w-wepW -16, this.y+this.h-wepH,wepW,wepH);
				swingCount++;
				if(swingCount>=(spriteRate/3)){
					swing--;
					swingCount = 0;
				}
			}
			screen.drawImage(charSprite, this.w*animState, 0,this.w, this.h, this.x, this.y, this.w, this.h);
		}
	}
	this.jump = function(){
		if(this.jumps>0){
			this.xCheck();
			this.yVel = -jumpPower;
			this.y = this.y-jumpPower;
			this.jumps--;
		}
	}
	this.attack = function(){
		if(swing == 0){
			swing = wepDur;
		}
	}
}

green = new Character(100,100,"green",true);
red = new Character(50,50,"red",false);
blue = new Character(0,0,"blue",false);