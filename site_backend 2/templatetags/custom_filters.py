from django import template
from django.utils.html import mark_safe
import site_backend.models as models
from django.db.models import Sum, Count


register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def plus(value, arg):
    return value * arg

@register.filter
def divide(value, arg):
    return value / arg


@register.filter
def count_percent(value, percent):
    try:
        return value * percent / 100
    except:
        return 0


@register.filter
def count_user_percent(value, percent):
    try:
        user_percent = 100 - percent
        return value * user_percent / 100
    except:
        return 0


@register.filter
def get_ammount_active_deal(str):
    return models.Deals.objects.filter(status__in=[1, 2, 3]).aggregate(Count('id'))['id__count']


@register.filter
def get_ammount_blocked_users(str):
    return models.Employees.objects.filter(status=3).aggregate(Count('id'))['id__count']

@register.filter
def get_ammount_active_users(str):
    return models.Employees.objects.filter(status=1).aggregate(Count('id'))['id__count']

@register.filter
def get_ammount_frozen_users(str):
    return models.Employees.objects.filter(status=2).aggregate(Count('id'))['id__count']


@register.filter
def get_ammount_register_users(str):
    return models.Employees.objects.filter(status=0).aggregate(Count('id'))['id__count']


@register.filter
def get_wt_name(wt_id):

    try:
        return models.WorkType.objects.filter(id=wt_id['id_work_type_id']).values('type')[0]['type']
    except TypeError:
        return models.WorkType.objects.filter(id=wt_id).values('type')[0]['type']


@register.filter
def get_city_name(city_id):
    try:
        return models.City.objects.filter(id=city_id).values('city')[0]['city']
    except Exception:
        return 'err'


@register.filter
def do_abs(number):
    try:
        return abs(number)
    except TypeError:
        return number


@register.filter
def get_master_phone(id_master):
    try:
        print(id_master)
        print(models.Employees.objects.filter(id=id_master).values('phone'))
        return models.Employees.objects.filter(id=id_master).values('phone')[0]['phone']
    except Exception:
        return '-'

@register.filter
def add_emoji_if_excl(id_master):
    print(models.Employees.objects.filter(id=id_master).values('exclusive'))
    if models.Employees.objects.filter(id=id_master).values('exclusive')[0]['exclusive']:
        return '👑'
    else:
        return ''


@register.filter
def success_percent(id_master):
    complited_deals = models.Deals.objects.filter(id_user=id_master, status=4).aggregate(Count('id'))['id__count']
    if complited_deals == 0:
        return 0
    all_deals = models.Deals.objects.filter(id_user=id_master).aggregate(Count('id'))['id__count']
    if all_deals == 0:
        return 0
    return int(complited_deals/all_deals * 100)


@register.filter
def get_users_last_deal_comment(master_id):
    try:
        comment = models.Deals.objects.filter(id_user=master_id)[:1].values()[0]['comment']
        print('124 ', comment)
        if not comment:
            return None
        return comment
    except:
        return None


@register.filter
def get_users_last_deal_date(master_id):
    try:
        date = models.Deals.objects.filter(id_user=master_id)[:1].values()[0]['date_drop']
        print('date', date)
        if not date:
            return None
        return date
    except:
        return None



