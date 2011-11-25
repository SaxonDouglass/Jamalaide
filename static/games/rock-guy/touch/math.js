function getDist(a, b){ // player, cursor
	var acx = a.x + a.w / 2;
	var acy = a.y + a.h / 2;
	var bcx = b.x;
	var bcy = b.y;
	var dist = Math.sqrt((bcx - acx)*(bcx - acx) + (bcy - acy)*(bcy - acy));
	
	return Math.floor(dist);
}

function getDist2(a, bx, by){ // player, cursor
	var acx = a.x + a.w / 2;
	var acy = a.y + a.h / 2;
	var bcx = bx;
	var bcy = by;
	var dist = Math.sqrt((bcx - acx)*(bcx - acx) + (bcy - acy)*(bcy - acy));
	
	return Math.floor(dist);
}

function dist(ax, ay, bx, by){ // 2 vector coords
	var acx = ax;
	var acy = ay;
	var bcx = bx;
	var bcy = by;
	var dist = Math.sqrt((bcx - acx)*(bcx - acx) + (bcy - acy)*(bcy - acy));
	
	return Math.floor(dist);
}

function testCenter(a, b){ // player, cursor
	var acx = a.x + a.w / 2;
	var acy = a.y + a.h / 2;
	var bcx = b.sx;
	var bcy = b.sy;
	
	context.fillStyle = "white";
	context.fillRect(acx, acy, 10, 10);
	context.fillStyle = "blue";
	context.fillRect(bcx, bcy, 10, 10);
}

function pCenter(a){ // returns player center coords
	var acx = a.x + a.w / 2;
	var acy = a.y + a.h / 2;
	
	return { x: acx, y: acy };
}

function pBase(a){ // returns player base
	var abaseX = a.x + a.w / 2;
	var abaseY = a.h;
	
	return { x: aBaseX, y: aBaseY };
}