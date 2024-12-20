'''
# 요구사항 
- 사용자 정보 처리 (name, age, city)
    - 환영 메시지를 생성
    - 사용자의 나이에 따라 특정 할인율을 적용
    - 사용자 이름을 포함한 작별 메세지를 생성
'''

from typing import Tuple

class User:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def generate_welcome_message(self) -> str:
        return f"환영합니다, {self.name}님! {self.city}에서 오셨군요!"

    def calculate_discount(self) -> float:
        if self.age < 18:
            return 0.1  # 10% 할인
        elif self.age <= 25:
            return 0.05  # 5% 할인
        else:
            return 0

    def generate_bye_message(self) -> str:
        return f"안녕히 가세요, {self.name}님!"

def process_user_info(user: User) -> Tuple[str, float, str]:
    welcome_message = user.generate_welcome_message()
    discount = user.calculate_discount()
    bye_message = user.generate_bye_message()
    return welcome_message, discount, bye_message

def main():
    user = User(name='지수', age=23, city='서울')
    message, discount, bye_message = process_user_info(user)
    print(message, discount, bye_message)

if __name__ == "__main__":
    main()
