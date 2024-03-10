# -*- coding: utf-8 -*-
from django.db import models

class FieldsExampleModel(models.Model):

    # # auto_field = models.AutoField(verbose_name='AutoField')
    # # big_auto_field = models.BigAutoField(verbose_name='BigAutoField')
    big_integer_field = models.BigIntegerField(verbose_name='BigIntegerField')
    binary_field = models.BinaryField(verbose_name='BinaryField')
    boolean_field = models.BooleanField(verbose_name='BooleanField')
    char_field = models.CharField(verbose_name='CharField', max_length=1024)
    date_field = models.DateField(verbose_name='DateField')
    date_time_field = models.DateTimeField(verbose_name='DateTimeField')
    decimal_field = models.DecimalField(verbose_name='DecimalField', decimal_places=3, max_digits=10)
    duration_field = models.DurationField(verbose_name='DurationField')
    email_field = models.EmailField(verbose_name='EmailField')
    file_field = models.FileField(verbose_name='FileField')
    # file_path_field = models.FilePathField(verbose_name='FilePathField')
    float_field = models.FloatField(verbose_name='FloatField')
    # generated_field = models.GeneratedField(verbose_name='GeneratedField')
    generic_ip_address_field = models.GenericIPAddressField(verbose_name='GenericIPAddressField')
    # # image_field = models.ImageField(verbose_name='ImageField')
    integer_field = models.IntegerField(verbose_name='IntegerField')
    json_field = models.JSONField(verbose_name='JSONField')
    positive_big_integer_field = models.PositiveBigIntegerField(verbose_name='PositiveBigIntegerField')
    positive_integer_field = models.PositiveIntegerField(verbose_name='PositiveIntegerField')
    positive_small_integer_field = models.PositiveSmallIntegerField(verbose_name='PositiveSmallIntegerField')
    slug_field = models.SlugField(verbose_name='SlugField')
    # # small_auto_field = models.SmallAutoField(verbose_name='SmallAutoField')
    small_integer_field = models.SmallIntegerField(verbose_name='SmallIntegerField')
    text_field = models.TextField(verbose_name='TextField')
    time_field = models.TimeField(verbose_name='TimeField')
    url_field = models.URLField(verbose_name='URLField')
    uuid_field = models.UUIDField(verbose_name='UUIDField')


    class Meta:
        verbose_name = '필드 예시'
        verbose_name_plural = '필드 예시들'
        db_table = 'fields_example'


class Entry(models.Model):
    member_no = models.CharField(max_length=32, verbose_name='회원번호', null=True, default='', blank=True)
    user_id = models.CharField(max_length=32, verbose_name='유저 ID', null=True, default='', blank=True)
    name = models.CharField(max_length=64, verbose_name='이름', null=True, default=None, blank=True)
    lastname = models.CharField(max_length=32, verbose_name='성', null=True, default=None, blank=True)
    firstname = models.CharField(max_length=32, verbose_name='이름', null=True, default=None, blank=True)
    nickname = models.CharField(max_length=32, verbose_name='닉네임', null=True, default=None, blank=True)
    email = models.EmailField(max_length=64, verbose_name='이메일', null=True, default=None)
    phone = models.CharField(max_length=16, verbose_name='핸드폰 번호', null=True, default=None, blank=True)
    # birthday = models.DateField(verbose_name='생년월일', null=True, default='', blank=True)
    nation = models.CharField(max_length=16, verbose_name='국적', null=True, default='KR', blank=True)
    address = models.CharField(max_length=256, verbose_name='주소', null=True, default='', blank=True)
    device_uuid = models.CharField(max_length=256, verbose_name='디바이스UUID', null=True, default='', blank=True)
    campaign_code = models.CharField(max_length=64, verbose_name='대상 캠페인 코드', null=True, default='', blank=True)
    group = models.CharField(max_length=64, verbose_name='그룹', null=True, default='', blank=True)
    grade = models.CharField(max_length=64, verbose_name='등급', null=True, default='', blank=True)
    is_blacklist = models.BooleanField(verbose_name='블랙리스트', null=True, default=False, blank=True)
    is_privacy_policy_agreed = models.BooleanField(verbose_name='휴대폰 인증 여부', null=True, default=False, blank=True)
    contact_email = models.EmailField(max_length=64, verbose_name='연락이메일', null=True, default='', blank=True)
    browser = models.CharField(max_length=256, verbose_name='브라우저 버전', null=True, default='', blank=True)
    delivery_address = models.CharField(max_length=256, verbose_name='주소(배송지)', null=True, default='')
    privacy = models.JSONField(null=True, verbose_name='추가 개인정보', default=None)

    is_valid = models.BooleanField(verbose_name='유효성 검사 통과', default=False, null=False)
    validation_log = models.CharField(max_length=64, verbose_name='유효성 검사 로그', null=True, default='', blank=True)
    is_excluded = models.BooleanField(verbose_name='제외 여부', default=False, null=False)
    exclude_reason = models.CharField(max_length=64, verbose_name='제외 원인', null=True, default='', blank=True)

    channel = models.CharField(max_length=64, verbose_name='참여 채널', null=True, default='', blank=True)
    # applied_at = models.DateTimeField(verbose_name='참여 일시', null=True, default='2023-12-20 10:00:00', blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = '참여자'
        verbose_name_plural = '참여자 정보'
        db_table = 'entry'
