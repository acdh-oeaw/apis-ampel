# Generated by Django 3.2 on 2022-11-10 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_metainfo', '0006_remove_text_lang'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmpelTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('red', 'red'), ('yellow', 'yellow'), ('green', 'green')], default='red', max_length=300)),
                ('note', models.TextField(blank=True, max_length=2000, null=True)),
                ('temp_entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apis_metainfo.tempentityclass')),
            ],
        ),
        migrations.CreateModel(
            name='AmpelSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_active', models.BooleanField(default=False)),
                ('_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='AmpelGeneric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('red', 'red'), ('yellow', 'yellow'), ('green', 'green')], default='red', max_length=300)),
                ('note', models.TextField(blank=True, max_length=2000, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'unique_together': {('object_id', 'content_type')},
            },
        ),
    ]
