from operator import index
import random

# 1. 세자릿수 숫자를 만들어 저장하기
# 2. 안내 문구 표시 - "숫자를 입력하세요"
# 3. 입력 받기
# 4. 입력 받은 숫자와 저장된 숫자를 비교하기
# 5. 스트라이크와 볼로 표시하기. 예) 1S / 2B 1S / 1B 2S / 3S
# 6. 3S 이면 게임 끝

class Baseball:
    global strike, index_anserd
    global boll, chance
    strike = 0
    boll = 0
    chance = 0
    index_anserd = 0 #인데스로 대답을 하나씩 비교할때 쓰는 변수

    '''
    한줄 복사: Shift + Alt + 화살표
    한줄 이동 : Alt + 화살표
    한줄 삭제 : Cmd + Shift + k
    '''
    def make_correct_number(self):
        #print(self.a)   
        correct_numbers = []
        correct_numbers = random.sample(range(1, 10), 3)#세자릿수 만들어 정의하기
        return correct_numbers

    def input_anserd(self):
        anserd = input()
        return anserd

    def check_anserd(self, correct_numbers, anserd):
        global strike, index_anserd, boll, chance
        while strike < 3:
            if anserd == 'q':
                break
            if len(anserd) != 3:#숫자를 세개보다 많이쎃는 지 확인하는 코드
                result = "error"
                return result
            for correct in correct_numbers:
                correct_str = str(correct) 
                if anserd[index_anserd] == correct_str:
                    strike = strike + 1 
                    index_anserd = index_anserd + 1
                else:            
                    for anserd_boll in anserd:         
                        if correct_str == anserd_boll:
                            boll = boll + 1
                    index_anserd = index_anserd + 1 
            if strike != 3:
                result = "false"
            elif strike == 3:
                result = "true"
            else: 
                result = 'defeat'
            return result         


    def play_game(self):
        correct_numbers = self.make_correct_number()
        game_end = "false"#play_baseball을 계속 돌릴지 정할때 쓰는 변수
        while game_end == "false":
            print("숫자를 임력하세요. 같은 숫자 안됨. 예: 123")#안내문구 표시
            anserd = self.input_anserd()
            result = self.check_anserd(correct_numbers, anserd)
                #if anserd == 'q':
                #   print('실패하셨습니다.')
                #  print('정답:',correct_numbers)
            global strike, index_anserd, boll, chance
            if result == "false":
                print(strike,'s' ,boll,'b') 
                strike = 0
                boll = 0
                chance = chance + 1
                index_anserd = 0
                print('시도한 횟수:',chance,'(그만하고 싶으시면 q라고 쓰세요)')
            elif result == "true":
                game_end = "true"      
                print('시도한 횟수:',chance)
                print('축하합니다!!') 
                print(correct_numbers)
            elif result == 'error':
                print("똑바로 쓰세요")
            else:
                game_end = 'true'
                print('포기 하셨습니다.')
                print('정답:', correct_numbers)            


#correct_numbers = make_correct_number()
#myball = Making_Baseball

# Making Baseball Class 만
myball = Baseball()
#myball.make_correct_number()
myball.play_game()








#클래스 안에서 매계변수는 어떻게 도는가..(return등)..(61번 줄에 correct_numbers를 넣어야 되나)