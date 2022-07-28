from rest_framework import serializers

# Models
from auth_server.models import User
# Role serializer
from rolepermissions.roles import assign_role


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(style={'input_type': 'text'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'text'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'company', 'role']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'role': {'required': True},
            'company': {'required': True},
            'password': {'required': True},
            'password2': {'required': True},
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Email': 'Email already exists'})

        account = User(email=self.validated_data['email'],
                       company=self.validated_data['company'],
                       first_name=self.validated_data['first_name'],
                       last_name=self.validated_data['last_name'])
        account.set_password(password)
        account.save()
        user = User.objects.get(id=account.id)
        try:
            assign_role(user, self.validated_data['role'])
        except Exception as e:
            user.delete()
            raise serializers.ValidationError('invalid role')

