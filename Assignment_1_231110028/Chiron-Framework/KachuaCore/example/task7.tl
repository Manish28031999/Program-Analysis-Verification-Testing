pendown

if(:x>50 )[
repeat 5 [
    forward 10
    if(:y > 100)[
        right 60
        left 30
        backward 15
        forward 40
    ]else[
        left 35
        right 95
        forward 20
        backward 50
    ]
    if(:x <=100)[
        forward 10 
    ]else[
        backward 5
        forward 60
        
    ]
]]
else[
    
if(:x ==0)[
    left 80
    backward 100
]




if(:y > 80)[
    backward 20
]
]

