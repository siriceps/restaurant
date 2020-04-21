from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.cache import cache

from accounts.models import Account


def cache_account(account_id):
    key = 'account_%s' % account_id
    result = cache.get(key)
    if result is None:
        try:
            result = Account.objects.get(id=account_id)
        except:
            result = -1
        cache.set(key, result)
    return None if result == -1 else result


def cache_account_delete(account_id):
    key = 'account_%s' % account_id
    cache.delete(key)
    cache.delete('account_profile_%s' % account_id)


def cache_account_data_delete(account_id):
    key = 'account_data_%s' % account_id
    cache.delete(key)


def cached_auth_permission(user_id, group):
    if group is None:
        key = 'auth_permission_%s' % user_id
    else:
        key = 'auth_permission_%s_%s' % (user_id, group.id)
    result = cache.get(key)
    if result is None:
        user_groups_field = get_user_model()._meta.get_field('groups')
        user_groups_query = 'group__%s' % user_groups_field.related_query_name()
        perms = Permission.objects.filter(**{user_groups_query: user_id})
        if group is not None:
            perms = perms.filter(group=group)
        result = perms.values_list('content_type__app_label', 'codename').order_by()
        cache.set(key, result, get_time_out())
    return result


def cached_auth_group(group_id):
    key = 'auth_group_%s' % group_id
    result = cache.get(key)
    if result is None:
        try:
            result = Group.objects.get(id=group_id)
            cache.set(key, result, get_time_out())
        except:
            return None
    return result


def cached_auth_group_list(account):
    key = 'auth_group_list_%s' % account.id
    result = cache.get(key)
    if result is None:
        result = account.groups.all()
        cache.set(key, result, get_time_out())
    return result
