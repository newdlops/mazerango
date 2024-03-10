# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin
from .models import Entry, FieldsExampleModel
from django.contrib import admin
from mazerango.mazerango_admin import ModelAdmin

@admin.register(Entry)
class EntryAdmin(ModelAdmin):
    list_display = [
        'id', 'campaign_code',
        'member_no', 'user_id', 'name', 'nickname', 'email', 'phone', 'grade', 'channel',
        'is_privacy_policy_agreed', 'is_blacklist'
    ]
    list_display_links = ['member_no', 'id', 'campaign_code', 'name']

@admin.register(FieldsExampleModel)
class ExampleAdmin(ModelAdmin):
    exclude = []
    # list_display = [
    #     'big_integer_field',
    #     'binary_field',
    #     'boolean_field',
    #     'char_field',
    #     'date_field',
    #     'date_time_field',
    #     'decimal_field',
    #     'duration_field',
    #     'email_field',
    #     'file_field',
    #     'file_path_field',
    #     'float_field',
    #     'generic_ip_address_field',
    #     'integer_field',
    #     'json_field',
    #     'positive_big_integer_field',
    #     'positive_integer_field',
    #     'positive_small_integer_field',
    #     'slug_field',
    #     'small_integer_field',
    #     'text_field',
    #     'time_field',
    #     'url_field',
    #     'uuid_field',
    # ]
