/*
reactions-anywhere: http://bit.ly/2rh8fgx
website: http://bit.ly/2rdLEzi
*/

var webpack = require('webpack');
var path = require('path');

module.exports = {
	context: __dirname + "/Scripts",
	externals: {
		jquery: 'jQuery',
		bootstrap: "bootstrap"
	}
}