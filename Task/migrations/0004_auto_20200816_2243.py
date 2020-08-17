# Generated by Django 3.0.5 on 2020-08-16 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20200816_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={},
        ),
        migrations.AddField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[('input', 'input_box'), ('select', 'select_box')], default='input', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Task.Choices'),
        ),
    ]
