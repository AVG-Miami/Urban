from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    # указываем, что поле user должно быть скрытым и автоматически
    # заполняться данными текущего пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Students
        fields = "__all__"