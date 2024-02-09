![Pypi](https://img.shields.io/pypi/v/django-table-permissions?style=flat-square)
![Python](https://img.shields.io/pypi/pyversions/django-table-permissions?style=flat-square)
![Django](https://img.shields.io/badge/Django-4.0%7C4.1%7C4.2%7C5.0-green)


# Django Table Permissions

Display django permissions in a user friendly, translatable and customizable widget..

## Features

- Permissions and their relevant app and models names are displayed in the active language.
- Permissions are displayed in a table that contain the default model permissions plus any custom permissions.
- Supports view permission (started with Django 2).
- Customize which apps, models to show in the permissions table. You can also set a exclude function for high-end customization.
- RTL ready, Bootstrap ready.
- Easy customize-able look.
- Python 3.10, 3.11, 3.12 Django 4.0, 4.1, 4.2, 5.0
- Default FilteredSelectMultiple widget will appear only if you have custom permissions that are not model related (ie directly created by code or hand)

## Installation

You can install django-table-permissions with pip by typing:

    pip install django-table-permissions

Or with poetry by typing::

    poetry add django-table-permissions

and add "table_permissions" to your INSTALLED_APPS setting (at any place after django.contrib.auth)

```python
INSTALLED_APPS = [
    'django.contrib.auth',
     ....
    'table_permissions',
]
```
Finally, execute:

```python
python manage.py collectstatic
```
then navigate to User and/or Group change form to see table_permissions in action.

## Configurations

Table permissions possible configurations and their default:

```python
TABLE_PERMISSIONS_CONFIG = {
    "template": "table_permissions/admin/table_permissions.html",
    "js_file": "table_permissions/table_permissions.js",
    "exclude": {
        "override": False,
        "apps": [],
        "models": [],
        "function": "table_permissions.helpers.dummy_permissions_exclude",
    },
    "auto_implement": True,
    "use_for_concrete": False,
    "custom_permission_translation": "table_permissions.helpers.custom_permissions_translator",
    "apps_customization_func": "table_permissions.helpers.apps_customization_func",
    "custom_permissions_customization_func": "table_permissions.helpers.custom_permissions_customization_func",
}
```

### _template_

The template which contains the permissions table, you can always customize this template by extending or overriding. Notice that there is a style block which you can override to easily edit the css.

### _js\_file_

You can change this file for add your custom javascript code. Read how it works below.

### _exclude_

Control which apps, models to show in the permissions table.

By default `table_permissions` exclude sessions , contenttypes and admin apps from showing their models in the permissions table. If you want to show them you can switch override to `False`.

apps & models lists would contain the names of the apps and models you wish to exclude.

function is a dotted path of a custom function which receive the model as a parameter to decide either to exclude it or not, default to a dummy function that always return `False` (ie do not exclude)

### _auto\_implement_

By default, just by including `table_permissions` in your installed_apps, the `django.contrib.admin.UserAdmin` (and GroupAdmin) are "patched" to include the `table_permissions` widget. If you have a custom UserAdmin, then set this option to False and make sure you either:

Inherit from `table_permissions.admin.TablePermissionsUserAdmin` and `table_permissions.admin.TablePermissionsGroupAdmin` for User & Group ModelAdmin.

Or for a more direct and compact way, inherit your ModelAdmin from `table_permissions.admin.UserTablePermissionsMixin` and `table_permissions.admin.GroupTablePermissionsMixin` (comes before `admin.ModelAdmin` in the mro),
Set the `user_permissions` widget to `table_permissions.widgets.TablePermissionsWidget` and remember to send a 3rd argument 'permissions' for Group Model Admin.
See `table_permissions.admin` for information.

### _use\_for\_concrete_ (DEPRECATED)
`Default: False`

Will be remove on the next version

### _custom\_permission\_translation_
A dotted path function to translate the custom permission. This function gets passed the permissions codename, verbose_name and its relevant content_type_id. The function will try to translate the permission verbose_name.

### _apps\_customization\_func_
A dotted path function to control the whole permissions objects passed to the widget. Sometimes you use custom menu where apps and models are ordered in a more "user friendly" manner and not necessarily in the "actual programmatic" apps & models order. You can use this option to get a hold of the whole ordered dict and shuffle its content around moving models from one app to the other and do all kind of crazy stuff to get just the right table of permissions.

### _custom\_permissions\_customization\_func_
A dotted path function to control the "extra" permissions which will be displayed on the default django widget. Suppose a model is removed, or an app is commented out of `INSTALLED_APPS`; its permissions are still in the permissions table, and it will be picked up.

Use this function to manipulate and order those permissions and return them . The permissions are passed a list of tuples , like this `[(perm_id, perm_name), (perm_id, perm_name), ...]`

## JavaScript
Located at `static/table_permissions/table_permissions.js`, it have 2 responsibilities:

- Upon form submit, the checked permissions in the table are dynamically appended to the form default permission input so the backend can carry on its functionality normally and correctly.
- Add handlers for column and row select-all checkboxes.

## Demo
To run the demo project in the repo on your local you need

- Clone the repo;
- Create a virtualenv
```bash
$ pip install django-table-permissions
$ cd demo_proj
$ python manage.py migrate
$ python manage.py runserver
```

## Test
