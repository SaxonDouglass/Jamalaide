function update(){
	
	// move bomb
	if (player1.selected && gesture.current == "vertical"){
		player.action = "bomb";
		bomb.active = true;
		dropBomb();
	}
	
	// Move player to monster
	if (player1.target == "monster" &&
		player1.action == "attack" &&
		player1.x + player1.w < monster.x - 15){
		movePlayerToMonster(player1, monster, getDelta());
	}
	
	// Move player to destination
	if (player1.action == "move"){
		if (getDist2(player1, player1.dx, player1.dy) < 100){
			// stop player
			player1.action = null;
		} else {
			movePlayer(player1, getDelta());
		}
	} 
	
	// selected player set cursor
	isPlayerSelected();
}

function isPlayerSelected(){
// What to do if player is selected
	if (player1.selected){
		// Set cursor to under player
		cursor1.x = player1.x + player1.w / 2;
		cursor1.y = player1.y + player1.h;
		cursor1.visible = true;	
	} else if (!player1.selected)
		cursor1.visible = false;
}

function dropBomb(){
	if(bomb.active && !bomb.moving){
		bomb.x = monster.x + monster.w / 2 - bomb.w / 2;
		bomb.y = -100;
		bomb.moving = true;
	} else if (bomb.active && bomb.moving){
		bombMove();
	}
}

function bombMove(){
	var ymove = bomb.speed;
	bomb.y += ymove;
	if (bomb.y > (monster.y + monster.h)){
		bomb.active = false;
		bomb.moving = false;
		player1.action = null;
		gesture.current = null;
	}
}
