pendown
repeat 10 [
    forward 10
    if(:y > 230)[
        right 40
        forward 25
    ]else[
        left 40
        forward 20
    ]
    if(:x <= -15)[
        forward 10 
    ]else[
        backward 5
        :y = :x + 2*:y
    ]
]

if(:x > 0)[
    left 80
    backward 100
]




if(:y == 89)[
    backward 20
]
