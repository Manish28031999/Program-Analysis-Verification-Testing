pendown
if(:x>50 )[
    forward 10
    if(:y > 100)[
        forward 40
    ]else[
        left 60
    ]
    if(:x <=100)[
        forward 10 
    ]else[
        backward 5
    ]
]
else[
if(:x >0)[
    left 80
    backward 100
]]





