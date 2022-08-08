from rest_framework import serializers

# Models
from auth_server.models import User
from task_server.models import Company
# Role serializer
from rolepermissions.roles import assign_role
# Serializers
from task_server.api.serializers.company.index import CompanySerializer


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
            'company_name': {'required': True},
        }

    def save(self):
        try:
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
                print(self.validated_data)
                user.delete()
                company = Company.objects.get(description=self.validated_data['company'])
                company.delete()
                raise serializers.ValidationError('invalid role')
        except Exception as e:
            print(self.validated_data)
            company = Company.objects.get(description=self.validated_data['company'])
            company.delete()
            raise serializers.ValidationError(str(e))


class UserReadOonlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'company']
        read_only_fields = ['id', 'first_name', 'last_name', 'email', 'company']
