# Generated by Django 2.2 on 2023-02-22 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientno', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='客户编号')),
                ('clientname', models.CharField(default='', max_length=15, verbose_name='客户名称')),
                ('clientstreet', models.CharField(max_length=10, verbose_name='客户所在街道')),
                ('clientcity', models.CharField(max_length=10, verbose_name='客户所在城市')),
                ('clientstate', models.CharField(max_length=10, verbose_name='客户所在省(自治区、直辖市)')),
                ('clientzipcode', models.CharField(max_length=6, verbose_name='邮政编码')),
                ('clienttelno', models.CharField(default='', max_length=11, verbose_name='客户电话')),
                ('clientfaxno', models.CharField(blank=True, max_length=13, null=True, verbose_name='客户传真')),
                ('clientwebaddress', models.CharField(blank=True, max_length=50, null=True, verbose_name='客户网址')),
                ('contactname', models.CharField(max_length=10, verbose_name='联系人姓名')),
                ('contacttelno', models.CharField(max_length=11, verbose_name='联系人电话')),
                ('contactfaxno', models.CharField(blank=True, max_length=17, null=True, verbose_name='联系人传真')),
                ('clientemaliaddress', models.CharField(default='', max_length=20, verbose_name='联系人邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeno', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='雇员编号')),
                ('titleno', models.CharField(max_length=10, unique=True, verbose_name='职称编号')),
                ('title', models.IntegerField(choices=[(1, '董事长'), (2, '总裁'), (3, '总经理'), (4, '大区经理'), (5, '经理'), (6, '高级技工'), (7, '普通技工')], verbose_name='职称')),
                ('firstname', models.CharField(max_length=10, verbose_name='名字')),
                ('address', models.CharField(max_length=30, verbose_name='住址')),
                ('worktelno', models.CharField(max_length=11, verbose_name='工作联系方式')),
                ('hometelno', models.CharField(blank=True, max_length=11, null=True, verbose_name='家庭联系方式')),
                ('empemailaddress', models.CharField(max_length=20, verbose_name='邮箱')),
                ('socialscuritynumber', models.CharField(max_length=19, verbose_name='身份证号')),
                ('dob', models.DateField(verbose_name='出生日期')),
                ('position', models.CharField(blank=True, max_length=5, null=True, verbose_name='所在地')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='薪资')),
                ('datestarted', models.DateField(verbose_name='入职时间')),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('outletno', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='商店编号')),
                ('outletstreet', models.CharField(max_length=50, verbose_name='商店所在街道')),
                ('outletcity', models.CharField(max_length=20, verbose_name='商店所在城市')),
                ('outletstate', models.CharField(max_length=20, verbose_name='商店所在省')),
                ('outletzipcode', models.CharField(max_length=6, verbose_name='邮政编码')),
                ('outlettelno', models.CharField(default='', max_length=11, verbose_name='商店电话')),
                ('outletfaxno', models.CharField(blank=True, max_length=17, null=True, verbose_name='商店传真')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehlicenseno', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='车辆编号')),
                ('vehiclemake', models.CharField(max_length=20, verbose_name='制车厂')),
                ('vehiclemodle', models.CharField(max_length=20, verbose_name='车型')),
                ('color', models.CharField(max_length=10, verbose_name='颜色')),
                ('nodoors', models.CharField(max_length=20, verbose_name='车门号')),
                ('capacity', models.SmallIntegerField(verbose_name='车容量')),
                ('hirerate', models.SmallIntegerField(verbose_name='日租金')),
                ('outletno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Outlet', verbose_name='门店编号')),
            ],
        ),
        migrations.CreateModel(
            name='Rentalagreement',
            fields=[
                ('rentalno', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='租凭编号')),
                ('datestart', models.DateField(verbose_name='租凭开始日期')),
                ('timestart', models.TimeField(verbose_name='租凭开始时间')),
                ('datereturn', models.DateField(verbose_name='租凭结束日期')),
                ('timereturn', models.TimeField(verbose_name='租凭结束时间')),
                ('mileagebefore', models.CharField(max_length=100, verbose_name='租凭前里程数')),
                ('mileageafter', models.CharField(max_length=100, verbose_name='租凭后里程数')),
                ('policyno', models.CharField(blank=True, max_length=10, null=True, verbose_name='合同编号')),
                ('insurancecovertype', models.CharField(blank=True, max_length=10, null=True, verbose_name='保险种类')),
                ('insurancepremium', models.IntegerField(blank=True, null=True, verbose_name='保险费')),
                ('clientno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Client', verbose_name='客户编号')),
                ('vehlicenseno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Vehicle', verbose_name='车辆编号')),
            ],
        ),
        migrations.CreateModel(
            name='Outletmanager',
            fields=[
                ('managerno', models.IntegerField(primary_key=True, serialize=False, verbose_name='记录编号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('outletno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Outlet', verbose_name='商店编号')),
                ('titleno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Employee', to_field='titleno', verbose_name='职称编号')),
            ],
        ),
        migrations.CreateModel(
            name='Faultreport',
            fields=[
                ('faultreportno', models.CharField(default='', max_length=10, primary_key=True, serialize=False, verbose_name='检修编号')),
                ('datachecked', models.DateField(db_column='dataChecked', verbose_name='检查日期')),
                ('timechecked', models.TimeField(blank=True, db_column='timeChecked', null=True, verbose_name='检查时间')),
                ('comments', models.CharField(blank=True, max_length=50, null=True, verbose_name='评语')),
                ('employeeno', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Employee', verbose_name='雇员编号')),
                ('vehlicenseno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Vehicle', verbose_name='车辆编号')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='outletno',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Outlet', verbose_name='部门编号'),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('employeeno', 'titleno')},
        ),
    ]
