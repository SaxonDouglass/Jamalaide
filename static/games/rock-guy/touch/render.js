function drawPlayer(obj){
	// context.fillStyle = obj.color;
	// context.fillRect(obj.x, obj.y, obj.w, obj.h);
	var frame = obj.frame;
	var size = 128;
	var fireSprite = ASSET_MANAGER.getAsset('img/fireSprite.png');
	context.drawImage(fireSprite, frame * size, 0, size, size, obj.x, obj.y, size, size);
}
function drawPlayer2(obj){
	// context.fillStyle = obj.color;
	// context.fillRect(obj.x, obj.y, obj.w, obj.h);
	var frame = 5;
	var size = 128;
	var iceSprite = ASSET_MANAGER.getAsset('img/iceSprite.png');
	context.drawImage(iceSprite, frame * size, 0, size, size, obj.x, obj.y, size, size);
}

function drawMonster(obj){
	var frame = 0;
	var size = 256;
	var monster = ASSET_MANAGER.getAsset('img/monster.png');
	context.drawImage(monster, frame * size, 0, size, size, obj.x, obj.y, size, size);
}

function drawCursor(obj){
	context.fillStyle = obj.color;
	context.fillRect(obj.x - obj.w/2, obj.y - obj.h / 2, obj.w, obj.h);
}
function drawLine(obj){
	context.beginPath();
	context.moveTo(obj.x, obj.y);
	context.lineTo(obj.ex, obj.ey);
	context.lineWidth = 10;
	context.lineCap = "round";
	context.strokeStyle = obj.color;	
	context.stroke();
	context.closePath();
}

function drawMonsterArms(obj){
	context.fillStyle = obj.color;
	context.fillRect(obj.x, obj.y, obj.w, obj.h);
}

function drawBomb(){
	context.fillStyle = "red";
	context.fillRect(bomb.x, bomb.y, bomb.w, bomb.h);
}

function render(){
	drawMonster(monster);
	// drawMonsterArms(monsterArms);
	
	if (cursor1.visible){
		if (player1.selected){ 
			drawCursor(cursor1);
		} else if (player2.selected){
			drawCursor(cursor2);
		} else {
			drawCursor(cursor1);
		}
	}
	
	if (touch.on){ drawLine(pointerLine); }
	if (bomb.active && bomb.moving){ drawBomb(); }
	
	currentFrame();
	drawPlayer(player1);
	drawPlayer2(player2);
}

function currentFrame(){
	switch (player1.action){
		case "attack": player1.frame = 6; break;
		case "move": player1.frame = 2; break;
		case "bomb": player1.frame = 0; break;
		default: player1.frame = 5;
	}
}