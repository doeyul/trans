import turtle
import random
import time

# 1. 화면 기본 설정
wn = turtle.Screen()
wn.title("설치 없는 자동차 피하기 게임")
wn.bgcolor("white")
wn.setup(width=400, height=600)
wn.tracer(0)  # 화면 자동 업데이트를 꺼서 애니메이션을 부드럽게 만듦

# 2. 내 자동차 (파란색 직사각형)
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.setheading(90)  # 위쪽을 바라보게 설정
player.shapesize(stretch_wid=1.5, stretch_len=2.5)  # 직사각형 모양으로 늘리기
player.penup()
player.goto(0, -250)

# 3. 장애물 리스트 (빨간색 정사각형 여러 개)
obstacles = []
for _ in range(5):
    obs = turtle.Turtle()
    obs.shape("square")
    obs.color("red")
    obs.penup()
    # 화면 위쪽 랜덤한 위치에서 시작
    obs.goto(random.randint(-180, 180), random.randint(300, 600))
    obstacles.append(obs)

# 4. 점수 표시기
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"점수: {score}", align="center", font=("Courier", 20, "bold"))

# 5. 자동차 이동 함수
def move_left():
    x = player.xcor()
    if x > -170:  # 화면 왼쪽 밖으로 나가지 않도록 제한
        player.setx(x - 30)

def move_right():
    x = player.xcor()
    if x < 170:   # 화면 오른쪽 밖으로 나가지 않도록 제한
        player.setx(x + 30)

# 6. 키보드 입력 연결
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# 게임 속도 제어
speed = 3
game_over = False

# 7. 메인 게임 루프
try:
    while not game_over:
        wn.update()      # 화면 업데이트
        time.sleep(0.01) # 프레임 조절

        # 각 장애물을 아래로 이동
        for obs in obstacles:
            y = obs.ycor()
            obs.sety(y - speed)

            # 장애물이 화면 아래로 벗어나면 다시 위로 보내고 점수 증가
            if obs.ycor() < -300:
                obs.goto(random.randint(-180, 180), random.randint(300, 500))
                score += 10
                speed += 0.1  # 난이도 상승 (속도 증가)
                
                pen.clear()
                pen.write(f"점수: {score}", align="center", font=("Courier", 20, "bold"))

            # 충돌 검사 (자동차와 장애물 사이의 거리가 30 이하이면 충돌로 간주)
            if obs.distance(player) < 30:
                game_over = True

    # 게임 오버 메시지 표시
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
    wn.update()
    
    # 클릭하면 창 닫기
    wn.exitonclick()

except turtle.Terminator:
    # 게임 도중 창을 강제로 닫았을 때 발생하는 에러를 무시
    pass
