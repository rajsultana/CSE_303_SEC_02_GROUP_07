# Generated by Django 3.2.6 on 2021-08-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0009_assessments_t_evaluation_t_section_t_student_enrollment_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_t',
            name='course_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='department_t',
            name='department_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty_t',
            name='f_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty_t',
            name='l_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='plo_t',
            name='plo_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='program_t',
            name='program_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='program_t',
            name='program_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='school_t',
            name='school_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='school_t',
            name='school_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='student_t',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student_t',
            name='f_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student_t',
            name='l_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student_t',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student_t',
            name='street',
            field=models.CharField(max_length=60),
        ),
    ]