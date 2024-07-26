pendown
if(:x > -100 && :y <= 0)[
    forward 20
    :z = 0
    right 50
    if(:y < -5)[
        backward 50
        left 30
    ]
]
if(:x >= 0 && :y > 80)[
    forward 60
    left 160
    if(:y > 5)[
        backward 10
        left 70
    ]
]


