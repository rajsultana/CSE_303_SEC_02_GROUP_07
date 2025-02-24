# Generated by Django 3.2.6 on 2021-09-06 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessments_T',
            fields=[
                ('Assessment ID', models.IntegerField(primary_key=True, serialize=False)),
                ('assessments_name', models.CharField(max_length=20)),
                ('Total Marks', models.FloatField()),
                ('Obtain Marks', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_T',
            fields=[
                ('course_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_type', models.CharField(max_length=10)),
                ('No of credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('department_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('faculty_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30, null=True)),
                ('l_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('contact_no', models.CharField(max_length=15, null=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('street', models.CharField(max_length=40, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('faculty_type', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GFaculty_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=25)),
                ('join_date', models.DateTimeField()),
                ('Gfaculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.faculty_t')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='Program_T',
            fields=[
                ('program_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='spm.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('school_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('section_id', models.CharField(default=None, max_length=20, primary_key=True, serialize=False)),
                ('Section No', models.IntegerField()),
                ('semester_name', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('No of student', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.course_t')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.gfaculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='VC_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('VFaculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.faculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='Student_T',
            fields=[
                ('student_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30, null=True)),
                ('l_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('contact_no', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('street', models.CharField(max_length=60, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('Year of admission', models.IntegerField(null=True)),
                ('semseter', models.CharField(max_length=10, null=True)),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='spm.department_t')),
                ('program', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='spm.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Enrollment_T',
            fields=[
                ('Enrollment ID', models.IntegerField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.section_t')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.student_t')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_req_course_T',
            fields=[
                ('course_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Pre_req_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.course_t')),
            ],
        ),
        migrations.CreateModel(
            name='PLO_T',
            fields=[
                ('plo_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('plo_name', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_T',
            fields=[
                ('Evaluation ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Obtain Marks', models.FloatField()),
                ('Total Marks', models.FloatField()),
                ('assessments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.assessments_t')),
                ('student_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.student_enrollment_t')),
            ],
        ),
        migrations.AddField(
            model_name='department_t',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.school_t'),
        ),
        migrations.CreateModel(
            name='Department_Head_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('HODFaculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.faculty_t')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='Dean_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('DFaculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.faculty_t')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.school_t')),
            ],
        ),
        migrations.AddField(
            model_name='course_t',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.program_t'),
        ),
        migrations.CreateModel(
            name='CO_T',
            fields=[
                ('co_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.course_t')),
                ('plo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.plo_t')),
            ],
        ),
        migrations.AddField(
            model_name='assessments_t',
            name='co',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.co_t'),
        ),
        migrations.AddField(
            model_name='assessments_t',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.school_t'),
        ),
    ]
