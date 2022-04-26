from django.contrib import admin
from .models import (Role,
                     User,
                     UserSkills,
                     Cluster,
                     Project,
                     Goal,
                     CheckList,
                     Skill,
                     Vacancy,
                     ApplicationVacation,
                     ApplicationProject,
                     RatingProject,
                     RatingUser,
                     Message,
                     Chat,)
# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(UserSkills)
admin.site.register(Cluster)
admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(CheckList)
admin.site.register(Skill)
admin.site.register(Vacancy)
admin.site.register(ApplicationVacation)
admin.site.register(ApplicationProject)
admin.site.register(RatingProject)
admin.site.register(RatingUser)
admin.site.register(Message)
admin.site.register(Chat)