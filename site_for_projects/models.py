from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


class Role(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE,related_name='role.User+',)
    name = models.CharField(max_length=255)
    course = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


class UserSkills(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user.UserSkills+')
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE,related_name='skill.UserSkills+')
    confirmed = models.ManyToManyField('User', blank=True)


class Cluster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE,related_name='cluster.Project+')
    image = models.ImageField(upload_to='project_image')
    contact = models.CharField(max_length=255)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE,related_name='teacher.Project+')
    curator = models.ForeignKey('User', on_delete=models.CASCADE, blank=True,related_name='curator.Project+')
    students = models.ManyToManyField('User', blank=True)


class Goal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    goals_after = models.ManyToManyField('self', blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project.Goal+')
    is_done = models.BooleanField(default=False)
    name = models.CharField(max_length=255)


class CheckList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE,related_name='goal.CheckList+')


class Skill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)


class Vacancy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    COURSES = [
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс')
    ]
    name = models.CharField(max_length=255)
    need_course = MultiSelectField(choices=COURSES)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project.Vacancy+')
    skills = models.ManyToManyField('Skill')


class ApplicationVacation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user.ApplicationVacation+')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE,related_name='vacancy.ApplicationVacation+')
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE,related_name="chat.ApplicationVacation+",)
    accept_last_project = models.BooleanField(null=True, default=None)
    accept_future_project = models.BooleanField(null=True, default=None)


class ApplicationProject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user.ApplicationProject+')
    employer = models.ForeignKey('User', on_delete=models.CASCADE,related_name='employer.ApplicationProject+')
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE,related_name='chat.ApplicationProject+')
    accept_employer = models.BooleanField(null=True, default=None)


class RatingProject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user.RatingProject+')
    project_to_rating = models.ForeignKey('Project', on_delete=models.CASCADE,related_name='project_to_rating.RatingProject+')


class RatingUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user.RatingUser+')
    user_to_rating = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user_to_rating.RatingUser+')


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    text_message = models.CharField(max_length=255)
    who_write = models.ForeignKey('User', on_delete=models.CASCADE,related_name='who_write.Message+')
    attached_file = models.ImageField(upload_to='message_attached')
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE,related_name='chat.Message+')


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
