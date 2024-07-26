penup
if :x > 0 [
	if :y > 0 [
        right 60
		if :z > 50 [
            left 30
			forward 20
		]
		else 
        [
            forward 60
            backward 10
        ]
	]
	else [forward 100]
]
else [ right 30
    backward 10]