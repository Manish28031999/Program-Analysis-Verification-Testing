pendown
left 90
forward 50
if(:x > 100 && :y < 150)[
    right 30
    backward 30
]
if(:x > -100 && :y > 150)[
    right 46
    backward 59
]
if(:x < 300 && :y < -150)[
    left 50
    forward 90
]
if(:x >= -100 && :y <= -100)[
    backward 20
    left 60
    forward 34
]
if(:x < 200 && :y > 150)[
    left 60
]
if(:y < 100)[
    right 50
    forward 60
]
if(:x < 150 && :y < -300)[
    forward 50
    right 90
]
if(:x >= -100 && :y <= -1000)[
    forward 100
]