# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book1(models.Model):
    ï_sno = models.IntegerField(db_column='ï»¿SNO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book1'


class Book2(models.Model):
    ï_sno = models.IntegerField(db_column='ï»¿SNO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    subject1 = models.IntegerField(db_column='Subject1', blank=True, null=True)  # Field name made lowercase.
    subject2 = models.IntegerField(db_column='Subject2', blank=True, null=True)  # Field name made lowercase.
    subject3 = models.IntegerField(db_column='Subject3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book2'


class Book3(models.Model):
    ï_status = models.TextField(db_column='ï»¿Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    worker = models.TextField(db_column='Worker', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book3'


class Dept(models.Model):
    deptno = models.IntegerField(db_column='DEPTNO', blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    loc = models.CharField(db_column='LOC', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept'


class Employes(models.Model):
    empno = models.IntegerField(db_column='EMPNO')  # Field name made lowercase.
    ename = models.CharField(db_column='ENAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=9, blank=True, null=True)  # Field name made lowercase.
    mgr = models.IntegerField(db_column='MGR', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)  # Field name made lowercase.
    sal = models.IntegerField(db_column='SAL', blank=True, null=True)  # Field name made lowercase.
    comm = models.IntegerField(db_column='COMM', blank=True, null=True)  # Field name made lowercase.
    deptno = models.IntegerField(db_column='DEPTNO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employes'


class Sampleinvoice(models.Model):
    year_name = models.IntegerField(db_column='Year_Name', blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.TextField(db_column='invoiceNo', blank=True, null=True)  # Field name made lowercase.
    associatename = models.TextField(db_column='associateName', blank=True, null=True)  # Field name made lowercase.
    invoice_amount = models.IntegerField(db_column='Invoice_Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sampleinvoice'


class Sheet2(models.Model):
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fieldbonuseffectivestartdate = models.DateField(db_column='FIELDBONUSEFFECTIVESTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fieldbonuseffectiveenddate = models.DateField(db_column='FIELDBONUSEFFECTIVEENDDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sheet2'


class Sheet3(models.Model):
    zip = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet3'


class Sheet4(models.Model):
    zip = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet4'


class Task4Sheet2(models.Model):
    guid = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    fieldbonuseffectivestartdate = models.TextField(db_column='FIELDBONUSEFFECTIVESTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fieldbonuseffectiveenddate = models.TextField(db_column='FIELDBONUSEFFECTIVEENDDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task4_sheet2'


class Task4Sheet3(models.Model):
    ï_zip = models.TextField(db_column='ï»¿ZIP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task4_sheet3'


class Wandextract(models.Model):
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    worker = models.TextField(db_column='Worker', blank=True, null=True)  # Field name made lowercase.
    billrate = models.FloatField(blank=True, null=True)
    earnings = models.TextField(db_column='Earnings', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hours = models.FloatField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wandextract'
