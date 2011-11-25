function movePlayer(player, d){
	var dx = player.dx - player.x;
	var dy = player.dy - player.y;
	var m = Math.sqrt(dx*dx + dy*dy);
	var xmove = (dx / m) * player.speed * d;
	var ymove = (dy / m) * player.speed * d;
	player.x += xmove;
	player.y += ymove;
}

function movePlayerToMonster(player, obj, d){
	var dx = obj.x - player.x;
	var dy = obj.y + player.h - player.y;
	var m = Math.sqrt(dx*dx + dy*dy);
	var xmove = (dx / m) * player.speed * d;
	var ymove = (dy / m) * player.speed * d;
	player.x += xmove;
	player.y += ymove;
}