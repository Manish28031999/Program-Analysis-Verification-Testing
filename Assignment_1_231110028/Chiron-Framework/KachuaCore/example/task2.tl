pendown
:temp=0

if(:x< 0)
 [
    left 180
    :temp=-:x
    if(:temp>300)
    [ :temp=300]
    forward :temp
    if(:y>0)
    [
        right 90
        if(:y>400)
        [:y=300]
        forward :y
    ]

    else[
        left 90
        :temp=-:y
        if(:temp>400)
        [:temp=300]
        forward :temp
    ]
    
 ]



else
[
    if(:x>300)
    [ :x=300]
    forward :x
    if(:y>0)
    [
        left 90
        if(:y>400)
        [:y=300]
        forward :y
    ]

    else
    [
        right 90
        :temp=-:y
        if(:temp>400)
        [:temp=300]
        forward :temp
    ]

]




if(:m < 100)
 [
    forward 10
    
 ]
else
[
    backward 8
]