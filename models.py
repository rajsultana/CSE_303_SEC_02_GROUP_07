# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sheet1(models.Model):
    school_id = models.CharField(max_length=5, blank=True, null=True)
    school_name = models.CharField(max_length=44, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet1'


class SpmAssessmentsT(models.Model):
    assessment_id = models.IntegerField(db_column='Assessment ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    assessments_name = models.CharField(max_length=20)
    total_marks = models.FloatField(db_column='Total Marks')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obtain_marks = models.FloatField(db_column='Obtain Marks')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    co = models.ForeignKey('SpmCoT', models.DO_NOTHING)
    section = models.ForeignKey('SpmSchoolT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_assessments_t'


class SpmCoT(models.Model):
    co_id = models.CharField(primary_key=True, max_length=5)
    details = models.TextField()
    course = models.ForeignKey('SpmCourseT', models.DO_NOTHING)
    plo = models.ForeignKey('SpmPloT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_co_t'


class SpmCourseT(models.Model):
    course_id = models.CharField(primary_key=True, max_length=6)
    course_name = models.CharField(max_length=50)
    course_type = models.CharField(max_length=10)
    no_of_credits = models.IntegerField(db_column='No of credits')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    program = models.ForeignKey('SpmProgramT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_course_t'


class SpmDeanT(models.Model):
    id = models.BigAutoField(primary_key=True)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField()
    dfaculty_id = models.ForeignKey('SpmFacultyT', models.DO_NOTHING, db_column='DFaculty_id_id')  # Field name made lowercase.
    school = models.ForeignKey('SpmSchoolT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_dean_t'


class SpmDepartmentHeadT(models.Model):
    id = models.BigAutoField(primary_key=True)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hodfaculty_id = models.ForeignKey('SpmFacultyT', models.DO_NOTHING, db_column='HODFaculty_id_id')  # Field name made lowercase.
    department = models.ForeignKey('SpmDepartmentT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_department_head_t'


class SpmDepartmentT(models.Model):
    department_id = models.CharField(primary_key=True, max_length=10)
    department_name = models.CharField(max_length=50)
    school = models.ForeignKey('SpmSchoolT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_department_t'


class SpmEvaluationT(models.Model):
    evaluation_id = models.IntegerField(db_column='Evaluation ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    obtain_marks = models.FloatField(db_column='Obtain Marks')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_marks = models.FloatField(db_column='Total Marks')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    assessments = models.ForeignKey(SpmAssessmentsT, models.DO_NOTHING)
    student_enrollment = models.ForeignKey('SpmStudentEnrollmentT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_evaluation_t'


class SpmFacultyT(models.Model):
    faculty_id = models.CharField(primary_key=True, max_length=5)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=6)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    faculty_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'spm_faculty_t'


class SpmGfacultyT(models.Model):
    id = models.BigAutoField(primary_key=True)
    designation = models.CharField(max_length=25)
    join_date = models.DateTimeField()
    gfaculty_id = models.ForeignKey(SpmFacultyT, models.DO_NOTHING, db_column='Gfaculty_id_id')  # Field name made lowercase.
    department = models.ForeignKey(SpmDepartmentT, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_gfaculty_t'


class SpmPloT(models.Model):
    plo_id = models.CharField(primary_key=True, max_length=5)
    plo_name = models.CharField(max_length=50)
    program = models.ForeignKey('SpmProgramT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_plo_t'


class SpmPreReqCourseT(models.Model):
    course_id = models.CharField(primary_key=True, max_length=6)
    pre_req_course_id = models.ForeignKey(SpmCourseT, models.DO_NOTHING, db_column='Pre_req_course_id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spm_pre_req_course_t'


class SpmProgramT(models.Model):
    program_id = models.CharField(primary_key=True, max_length=10)
    program_name = models.CharField(max_length=50)
    department = models.ForeignKey(SpmDepartmentT, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_program_t'


class SpmSchoolT(models.Model):
    school_id = models.CharField(primary_key=True, max_length=10)
    school_name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'spm_school_t'


class SpmSectionT(models.Model):
    section_no = models.IntegerField(db_column='Section No', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    semester_name = models.CharField(max_length=10)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    no_of_student = models.IntegerField(db_column='No of student')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    course = models.ForeignKey(SpmCourseT, models.DO_NOTHING)
    faculty = models.ForeignKey(SpmGfacultyT, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_section_t'


class SpmStudentEnrollmentT(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrollment_id = models.IntegerField(db_column='Enrollment ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    semester = models.CharField(max_length=10)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    section = models.ForeignKey(SpmSectionT, models.DO_NOTHING)
    student = models.ForeignKey('SpmStudentT', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spm_student_enrollment_t'


class SpmStudentT(models.Model):
    student_id = models.CharField(primary_key=True, max_length=8)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateTimeField()
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    semseter = models.CharField(max_length=10)
    department = models.ForeignKey(SpmDepartmentT, models.DO_NOTHING)
    program = models.ForeignKey(SpmProgramT, models.DO_NOTHING)
    year_of_admission = models.IntegerField(db_column='Year of admission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'spm_student_t'


class SpmVcT(models.Model):
    id = models.BigAutoField(primary_key=True)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    vfaculty_id = models.ForeignKey(SpmFacultyT, models.DO_NOTHING, db_column='VFaculty_id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spm_vc_t'
