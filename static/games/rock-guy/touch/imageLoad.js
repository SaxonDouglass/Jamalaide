// Background Stuff
var bgcanvas = document.getElementById("bgcanvas");
var bgcontext = bgcanvas.getContext("2d");

function drawBG(){
// Background Colour
	bgcontext.fillStyle = "5D8DD8";
	bgcontext.fillRect(0, 0, 1024, 680);
}

// Furthest Tree Layers
var trees0 = new Image();
var trees1 = new Image();

trees0.src = "img/background_trees0.png";
trees1.src = "img/background_trees1.png";

function drawTrees(){
	trees0.onload = function(){
		bgcontext.drawImage(trees0, 0, 0);
	};
	trees1.onload = function(){
		bgcontext.drawImage(trees1, 0, 0);
		
		// Draw Ground
		bgcontext.fillStyle = "#A7896b";
		bgcontext.fillRect(0, 170, 1024, 680-170);
	};	
}

drawBG();
drawTrees();

/////////// Player Stuff
var ASSET_MANAGER = new AssetManager();
ASSET_MANAGER.queueDownload('img/fireSprite.png');
ASSET_MANAGER.queueDownload('img/iceSprite.png');
ASSET_MANAGER.queueDownload('img/monster.png');
ASSET_MANAGER.queueDownload('img/monsterarmleft.png');
ASSET_MANAGER.queueDownload('img/monsterarmright.png');