function Enemy(xIn, yIn){
	this.x = xIn;
	this.y = yIn;
	this.w = 48;
	this.h = 48;
	this.yVel = 0;
	this.xVel = 0;
	this.facing = -1;
	this.jumps = 0;
	var spriteRate = 3;
	var speed = 3;
	var acc = 1;
	var jumpCap = 1;
	var jumpPower = 15;
	var charSprite = new Image();
	charSprite.src="enemySprite.png";
	var attackSprite = new Image();
	attackSprite.src="slash.png";
	var animState = 0;
	var animCount = 0;
	var swing = 0;
	var swingCount = 0;
	
	this.xCheck = function(){
		if((this.x-30) > (you.x)){
			this.xVel = -speed;
			this.facing = -1;
		}else if((this.x+30) < (you.x)){
			this.xVel = speed;
			this.facing = 1;
		}else{
			this.xVel = 0;
		}
		//if(this.y>you.y && this.jumps>0){
		//	this.jump();
		//}
	}

this.compute = function(){
		if(this.y<(640-this.h)){
			this.yVel = this.yVel + acc;
			this.y = this.y + this.yVel;
			animState = 1;
		}else{
			this.xCheck();
			this.y = 640-this.h;
			this.yVel = 0;
			this.jumps = jumpCap;
			if(this.xVel == 0){
				animState = 0;
			}else{
				animCount++;
				animState = 1+Math.floor((animCount/spriteRate)%4);
			}
			if(you.y<540-you.h){
				this.jump();
			}
		}
		this.x += this.xVel;
	}
	this.draw = function(){
		if(this.facing == 1){
			screen.drawImage(charSprite, 48*animState, 48,this.w, this.h, this.x, this.y, this.w, this.h);
			if(swing > 0){
				screen.drawImage(attackSprite, 16*(swing-1), 48, 16,48, this.x+48, this.y, 16,48);
				swingCount++;
				if(swingCount>=spriteRate){
					swing--;
					swingCount = 0;
				}
			}
		}else{
			screen.drawImage(charSprite, 48*animState, 0,this.w, this.h, this.x, this.y, this.w, this.h);
			if(swing > 0){
				screen.drawImage(attackSprite, 48-(16*swing),0, 16,48, this.x-16, this.y, 16,48);
				swingCount++;
				if(swingCount>=spriteRate){
					swing--;
					swingCount = 0;
				}
			}
		}
	}
	this.jump = function(){
		if(this.jumps>0){
			this.yVel = -jumpPower;
			this.y = this.y-jumpPower;
			this.jumps--;
		}
	}
	this.attack = function(){
		if(swing == 0){
			swing = 4;
		}
	}
}
