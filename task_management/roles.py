from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'add_user': True,
        'update_user': True,
        'delete_user': True,
        'view_role': True,
        'add_role': True,
        'update_role': True,
        'delete_role': True,
        'list_team': True,
        'add_team': True,
        'update_team': True,
        'delete_team': True,
        'view_permission': True,
        'add_permission': True,
        'delete_permission': True,
    }


class Manager(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'list_team': True,
        'add_team': True,
        'update_team': True,
        'delete_team': True,
        'view_permission': True,
        'add_permission': True,
        'delete_permission': True,
    }


class Regular(AbstractUserRole):
    available_permissions = {
        'view_user': True
    }