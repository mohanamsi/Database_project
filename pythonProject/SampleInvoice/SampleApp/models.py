from django.db import models

# Create your models here.


class employes(models.Model):
    empno = models.IntegerField(db_column='EMPNO')  # Field name made lowercase.
    ename = models.CharField(db_column='ENAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=9, blank=True, null=True)  # Field name made lowercase.
    mgr = models.IntegerField(db_column='MGR', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)  # Field name made lowercase.
    sal = models.IntegerField(db_column='SAL', blank=True, null=True)  # Field name made lowercase.
    comm = models.IntegerField(db_column='COMM', blank=True, null=True)  # Field name made lowercase.
    deptno = models.IntegerField(db_column='DEPTNO', blank=True, null=True)  # Field name made lowercase.
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'employes'
#

    def __str__(self):
        return self.ename
