# SimpleJWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Roles and permissions
from rolepermissions.roles import get_user_roles


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        roles = []
        is_admin = False
        token = super().get_token(user)
        for role in get_user_roles(user):
            if role.__name__.lower() == 'admin':
                is_admin = True
            else:
                roles.append(role.__name__.lower())
        # Add custom claims
        token['name'] = f'{user.first_name} {user.last_name}'
        token['company_id'] = user.company.id
        token['company_name'] = user.company.description
        token['roles'] = roles
        token['is_admin'] = is_admin

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
