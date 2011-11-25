var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

var player = function(){
	return {
	x: 200,
	y: 400,
	w: 128,
	h: 128,
	dx: 0,
	dy: 0,
	m: 0, // magnitude
	color: "green",
	flip: false,
	selected: false,
	moving: false,
	speed: 300,
	distanceToTarget: 0,
	destX: 0,
	destY: 0,
	target: null,
	action: null,
	frame: 5
	};
};
// Create the players
var player1 = new player();
var player2 = new player();
var player1MoveTo = {
	x: 0,
	y: 0
};

// Cursor
var cursor1 = {
	x: 5, // Start X
	y: 5, // Start Y
	w: 150,
	h: 64,
	dx: 0, // Destination X
	dy: 0, // Destination Y
	visible: false,
	color: "#FFE135",
	radius: 96,	
};

var cursor2 = {
	x: 5, // Start X
	y: 5, // Start Y
	w: 150,
	h: 64,
	dx: 0, // Destination X
	dy: 0, // Destination Y
	visible: false,
	color: "#89CFF0",
	radius: 96,	
};

// Line
var pointerLine = {
	sx: 0,
	sy: 0,
	ex: 0,
	ey: 0,
	visible: 0,
	color: "#A8E4A3"
};

var touch = {};

var monster = {
	x: 0,
	y: 0,
	w: 256,
	h: 256,
	color: "red"
};

var monsterArms = {
	x: monster.x + monster.w - 40,
	y: monster.y + 10,
	x: 0,
	y: 0,
	w: 50,
	h: 125,
	color: "#CC0000"
};

var test1 = document.getElementById("test1");
var gesture = {
	sx: 0,
	sy: 0,
	ex: 0,
	ey: 0,
	current: null
};

var bomb = {
	x: 0,
	y: 0,
	w: 100,
	h: 100,
	speed: 50,
	active: false,
	moving: false
};