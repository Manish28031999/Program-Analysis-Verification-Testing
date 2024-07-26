pendown
if(:x > -100 && :y <= 0)[
    forward 20
    :z = 0
    right 50
    goto(20, -19)
    backward 9
    right 90
    forward 10
    if(:y < -5)[
        right 30
        forward 5
        left 30
    ]
]

if(:x >= 0 && :y > 80)[
    backward 15
    right 25
    forward 30
    left 160
    goto(10, 20)
    if(:y > 5)[
        right 60
        backward 10
        left 70
    ]
]

else[
    backward 40
    :z = :z * 90    
    right 90
    forward 20
    left 165
    goto(25,25)
    right 90
    forward 32
    backward 10
    left 170
    goto(-20, 8)
    if(:y > 5)[
        right 60
        backward 8
        left 60
    ]
]
