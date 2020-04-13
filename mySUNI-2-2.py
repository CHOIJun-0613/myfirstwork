import random

"""
랜덤한 숫자 세 자리를 만드는 함수인 rand()를 작성합니다.
1. 0으로 채워진 세 칸짜리 randnum 리스트를 만듭니다.
2. 0,1,2번째 인덱스의 값을 0부터 9까지 임의로 넣어주세요.
3. 0번째 인덱스와 1번째 인덱스가 다를 때 까지 1번째 인덱스의 값을 다시 설정하세요.
4. 0번째 인덱스와 2번째 인덱스 혹은 1번째 인덱스와 2번째 인덱스의 값이 다를 때 까지 
   2번째 인덱스의 값을 다시 설정하세요.
5. 만들어진 randnum 리스트를 리턴하세요.
"""
def rand():
    randnum = [0,0,0]
    cnt = 0
    while cnt < 3 :
        num = random.randrange(1, 10)
        if (num not in randnum) :
            randnum[cnt]= num
            cnt += 1
    return randnum

"""
야구 게임을 하는 함수인 baseball()을 생성합니다.
1. 필요한 변수 세 개를 만드세요.(strike, ball, cnt)
2. 지문의 예시와 동일하게 작동하도록 반복문을 만들어주세요.
    2-1. input 함수를 사용하여 사용자에게 입력을 받으세요.
    2-2. 2중 반복문을 이용하여 사용자의 숫자와 매개변수의 숫자를 비교하고, strike와 ball을 증가시키는 반복문을 만들어주세요.
    2-3. 한 번의 루프가 끝났다면 횟수 변수를 1 증가 시킵니다.
    2-4. 스트라이크와 볼의 갯수를 출력해주세요.
    2-5. 3 strike가 될 시에 반복문을 탈출하세요.
    2-6. 3 strike가 아니라면 strike와 ball을 0으로 만들어 다음 루프를 준비합니다.
3. 증가시킨 cnt 변수의 값을 출력합니다.
"""
def baseball(randnum):
    strike = 0
    ball = 0
    cnt = 0
 
    # strike와 ball을 증가시키는 반복문을 만들어주세요!
    while True:
        in_vars = input()
        randnum1 = randnum.copy()
        print("input value =", in_vars, "random =", randnum1)
        if ( len(in_vars) != 3 ) :
            print("3개의 숫자를 입력하세요.")
            continue

        for i in range(0, len(in_vars)) :
            if(int(in_vars[i]) in randnum1) :
                strike += 1
                randnum1.remove(int(in_vars[i]))
            else :
                ball += 1
            
        # 2-3. 한 번의 루프가 끝났다면 횟수 변수를 1 증가 시킵니다.
        cnt += 1
        
        # 2-4. 스트라이크와 볼의 갯수를 출력해주세요.
        print("스트라이크:", strike)
        print("볼:", ball)
        
        
        # 2-5. strike가 될 시에 반복문을 탈출!
        if strike == 3:
            break
        # 2-6. 3 strike가 아니라면 strike와 ball을 0으로 만들어 다음 루프를 준비합니다.
        else:
            strike = 0
            ball = 0 
    print(cnt,"번 만에 맞췄습니다!")

def main():
    randnum = rand()
    baseball(randnum)

if __name__ == "__main__":
    main()