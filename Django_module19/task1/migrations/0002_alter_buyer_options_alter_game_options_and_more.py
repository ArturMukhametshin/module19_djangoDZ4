# Generated by Django 4.2.17 on 2024-12-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-cost'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Баланс'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя покупателя'),
        ),
        migrations.AlterField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(related_name='games', to='task1.buyer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Размер файла'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
