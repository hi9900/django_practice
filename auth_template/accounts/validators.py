import string
from django.core.exceptions import ValidationError

def contains_special_character(value):
    for char in value:
        # string.punctuation에는 특수문자들이 저장되어 있습니다! 
        if char in string.punctuation: 
            return True  # 그걸 이용해서 특수문자를 걸러낼 수 있습니다!
    return False
    
# password는 class형 validator 사용해야 함
class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
            len(password) < 8 or
            not contains_uppercase_letter(password) or
            not contains_lowercase_letter(password) or
            not contains_number(password) or
            not contains_special_character(password)
        ):
            # 비밀번호가 유효하지 않으면
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    # admin 페이지에서 비밀번호를 바꿀 때 필요한 내용
    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")