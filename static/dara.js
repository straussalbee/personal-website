


document.addEventListener("DOMContentLoaded", function(event) {


	var i = 1234;
	var s = "asdf";
	var l = [1, 2,3, 4, 5, 6];
	var o = {
		"me": "yo",
		"asdf": 456,
		"now": "asdf"
	};
	o["hi"] = 7;
	o.hi = 8;


	for (var i = 0; i < l.length; i++) {
		console.log(l[i]);
	};


	// console.log(o["hi"])
	// console.log(o.hi)

	// console.log(i, s, l, o);

	// console.log("DOM fully loaded and parsed",event);
});

console.log("Hello world")