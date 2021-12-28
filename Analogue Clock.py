from turtle import *
from datetime import datetime

def jump(distance, a=0):
    penup()
    right(a)
    forward(distance)
    left(a)
    pendown()

def hand(ab, cd):
    fd(ab*1.15)
    rt(90)
    fd(cd/2.0)
    lt(120)
    fd(cd)
    lt(120)
    fd(cd)
    lt(120)
    fd(cd/2.0)

def make_hand_shape(name, ab, cd):
    reset()
    jump(-ab*0.15)
    begin_poly()
    hand(ab, cd)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray80", "gray90")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("gray10", "gray15")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("gray10", "gray15")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.bk(85)

def days(t):
    days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return days[t.weekday()]

def month(z):
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = months[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    try:
        tracer(False)  
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(days(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(month(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        tracer(True)
        second_hand.setheading(6*second)  
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*hour)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
