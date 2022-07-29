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
        'view_permission': True,
        'add_permission': True,
        'delete_permission': True,
        'view_team': True,
        'add_team': True,
        'update_team': True,
        'delete_team': True,
        'view_team_role': True,
        'add_team_role': True,
        'update_team_role': True,
        'delete_team_role': True,
    }


class Manager(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'add_user': True,
        'update_user': True,
        'delete_user': True,
        'view_permission': True,
        'add_permission': True,
        'delete_permission': True,
        'view_team': True,
        'add_team': True,
        'update_team': True,
        'delete_team': True,
        'view_team_role': True,
        'add_team_role': True,
        'update_team_role': True,
        'delete_team_role': True,
    }


class Worker(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'add_user': True,
        'update_user': True,
        'delete_user': True,
        'view_role': True,
        'view_permission': True,
        'view_teams': True,
        'view_team_roles': True,
    }