from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
# "메타데이터(metadata)"는 다른 데이터를 설명하거나 식별하는 데이터의 일종입니다. 즉, 메타데이터는 다른 정보나 데이터의 특성, 구조, 관계, 속성, 원본, 시간 등에 대한 정보를 제공합니다. 메타데이터는 주로 데이터의 관리, 검색, 분류, 이해, 활용, 보안 및 문서화를 돕는 데 사용됩니다.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')



