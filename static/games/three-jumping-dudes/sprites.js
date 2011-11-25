function Sprite(srcIn, wIn, hIn){
	this.image = new Image();
	this.image.src = srcIn;
	this.w = wIn;
	this.h = hIn;
	this.anim = 0;
}
function Sprite(srcIn, wIn, hIn, frameCount, rowCount){
	this.image = new Image();
	this.image.src = srcIn;
	this.w = wIn;
	this.h = hIn;
	this.anim = frameCount;
	this.animRow = rowCount;
}