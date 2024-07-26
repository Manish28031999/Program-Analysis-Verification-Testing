if(:x <= -100)[
    if(:y >= 90)[
        backward 100
        left 60
        forward 200
    ]
]

if(:x >= 209)[
    repeat 6[
        forward 100
        right 89
        backward 11
    ]
]

if(:x <= 100)[
    if(:y > 250)[
        backward 100
    ]
    if(:y < 0)[
        left 100
    ]
]