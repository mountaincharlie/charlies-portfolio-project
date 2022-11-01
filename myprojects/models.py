from django.db import models


class Technology(models.Model):
    """
    Inherits Django's models.Model and represents the Technology table in the
    database
    Contains the fields:
    name - required and must be unique
    """
    name = models.CharField(max_length=260, unique=True)

    class Meta:
        """ meta data for how to order technologies """
        ordering = ['name']

    def __str__(self):
        return self.name


# maybe - for listing key features of a project
# class Feature(models.Model):
#     """
    
#     """
#     name = models.CharField(max_length=260, unique=True)
#     icon =

#     def __str__(self):
#         return self.name



class Project(models.Model):
    """
    Inherits Django's models.Model and represents the Project table in the
    database
    Contains the fields:
    name - required and must be unique
    desktop_img - screenshot from the desktop view
    mobile_img - screenshot from the mobile view
    description - overview of the project's function/feats
    tech_used - list of technologies used in the project
    slug - unique identifier for each project (used in the urls to
    protect project id's being visible to users)
    public - BooleanField False by default, only visible onsite if True
    in_progress - BooleanField which is True for not yet complete projects which are public 
    live_link - link to the deployed site
    repo_link - link to the repo (to show the README)
    created_date - date the projectis added to the DB
    """
    name = models.CharField(max_length=260, unique=True)
    desktop_img =
    mobile_img =
    # video = [future feat]
    description = 
    # features?
    tech_used = 
    slug = 
    public = 
    in_progress =  # for not yet complete projects which are public
    live_link =
    repo_link =
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ meta data for how to order genres """
        ordering = ['created_date']

    def __str__(self):
        return self.name