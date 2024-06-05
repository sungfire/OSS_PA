# 무한의 계단

---

# 구현 목표

### 본 프로젝트는 휴대폰 게임인 무한의 계단을 구현한 것으로, 방향을 바꿔가며 계단을 많이 오르는 것을 목표로 하는 게임입니다. 움직인 곳에 계단이 없거나, 타이머가 끝날 때까지 움직이지 못하면 패배합니다.

---

# 구현 기능

1. pygame 기반 게임환경 구현
2. 스페이스바 입력으로 방향 조정 기능
3. 왼쪽 쉬프트로 움직임 구현
4. 타이머, 계단 랜덤 생성 구현

---

# 실행 방법

```
1. python3.12 를 설치한다.

2. pygame library 를 설치한다. (pip3 install pygame)

3. 재부팅 이후 main.py가 있는 폴더에서 파일을 실행하면 게임이 실행됨. (python3 main.py) 

```

---

# 실행 예시

![Infinite_stairs](https://github.com/sungfire/OSS_PA/assets/82808698/8e73533f-544d-4367-a6a5-0d62df1c3cea)

---

# 코드 설명
## main.py
### class Player
    - 사용자가 움직이는 캐릭터
    1. def __init__ : 최초 player의 크기와 위치, 이미지 설정
    2. def change_direction : 사용자의 이동 방향 변경
    3. def : 사용자의 실제 이동 구현

### class Stair
    - Player가 이동해야하는 계단
    1. def __init__ : 계단 이미지, 크기 위치에 맞게 계단 생성
    2. def update : 사용자가 움직일 때 계단의 위치 조정으로 사용자가 움직이는 것 같이 만들기 위해 계단의 위치 변경

### def add_new_stair
    - Player가 움직여서 계단이 내려오면 맨 위에 새로운 계단을 만드는 함수

### def init_game
    - 새로운 게임을 시작하는 함수

### def check_stair_below_player
    - Player가 이동한 곳에 계단이 있는지 확인하는 함수

### Main loop
    - 실제 게임 루프
    1. 왼쪽 shift를 누르면 Player가 이동하며 게임 시작.
    2. 상단 바가 모두 빨간색으로 변하기 전에 움직이지 않으면 패배.
    3. 계단이 없는 곳으로 이동해도 패배.
    4. 5칸 오를 때마다 time_limit을 줄여서 게임 난이도 상향
    5. 오른쪽 shift 누르면 임의로 게임 중단.

---


    




