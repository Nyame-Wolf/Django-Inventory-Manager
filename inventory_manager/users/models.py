from django.db import models

# to create a custom user:
from django.contrib.auth.models import AbstractUser

# create a custom user as recommended by django doc class


class CustomUser(AbstractUser):
    pass

    class Meta:
        permissions = (
            ("can_report_lost_asset", "Can report lost assets"),
            ("can_report_lost_and_found_asset",
             "Can report lost and found assets"),
            ("can_see_assigned_assets_list",
             "Can see a list of assigned assets"),
            ("can_see_unassignied_assets_list",
             "Can see a list of unassigned assets"),
            ("can_see_assigned_items_history",
             "Can see history of assests assigned"),
            ("can_add_user_to_staff_group", "Can add user to staff group"),
            ("can_view_users_in_staff_group", "Can view users in staff group"),
            ("can_delete_users_in_staff_group", "Can delete users in staff group"),
            ("can_change_users_in_staff_group", "Can change users in staff group"),
            ("can_add_users_to_admin_group", "Can add users to admin group"),
            ("can_view_users_in_admin_group", "Can view users in admin group"),
            ("can_delete_users_in_admin_group", "Can delete users in admin group"),
            ("can_change_users_in_admin_group", "Can change users in admin group"),

        )

    def __str__(self):
        return self.username
