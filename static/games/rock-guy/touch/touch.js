function setTouch(e){
	touch = { x: e.touches[0].pageX, y: e.touches[0].pageY, on: true };
}

function setLineEnd(x,y){
	pointerLine.ex = x;
	pointerLine.ey = y;
}

function touchMove(e){
	e.preventDefault();
	if(e.touches){
		setTouch(e);
		pointerLine.ex = touch.x;
		pointerLine.ey = touch.y;
	}
}

function touchStart(e){
	e.preventDefault();
	if (e.touches){
		setTouch(e);
		var x = e.touches[0].pageX;
		var y = e.touches[0].pageY;	
	
		if (getDist(player1, touch) < 128){
			// snap tp player
			player1.selected = true;
			pointerLine.x = player1.x + player1.w / 2;
			pointerLine.y = player1.y + player1.h;
			pointerLine.ex = x;
			pointerLine.ey = y;
		} else if (!player1.selected && getDist(player1, touch) >= 128){
			// Player drags to empty space
			// Player not currently selected
			// This does nothing
			pointerLine.x = x;
			pointerLine.y = y;
			pointerLine.ex = x;
			pointerLine.ey = y;
		} else if (player1.selected && getDist(player1, touch) >= 128){
			// Player drags to empty space	
			// Player is selected
			// Action considered move
			player1.selected = true;
			cursor1.x = x;
			cursor1.y = y;
			pointerLine.x = x;
			pointerLine.y = y;
			pointerLine.ex = x;
			pointerLine.ey = y;
			if (player1.action == null){
				player1.dx = x;
				player1.dy = y;
			}
		}
		if (getDist(player2, touch) < 100){
			// player2.selected;
		}
	}
}

function touchEnd(e){
	// setTouch(e);
	touch.on = false;	

	currentGesture();
	
	if (gesture.current != "vertical"){ 
		if (player1.selected && getDist(monster, touch) < 192){
			// player selected, monster targeted, not vertical
			// attack monster 
			player1.target = "monster";
			player1.action = "attack";
			player1.dy = monster.x;
			player1.dx = monster.y + monster.h;
		} else if (player1.selected && getDist(player1, touch) > 100 ){
			// player selected, monster not targeted, not vertical
			// Move player
			player1.action = "move";
			player1.target = null;
			player1.dx = touch.x;
			player1.dy = touch.y;
		}
	}
}

function currentGesture(){
	var sx = pointerLine.x;
	var sy = pointerLine.y;
	var ex = pointerLine.ex;
	var ey = pointerLine.ey;
	if (Math.abs(ey - sy) > 400 && Math.abs(ex - sx) < 50){
		gesture.current = "vertical";
	} else if (Math.abs(ex - sx) > 400 && Math.abs(ey - sy) < 50){
		gesture.current = "horiztonal";
	} else {
		gesture.current = null;
	}
	// test1.innerHTML = gesture.current;
}