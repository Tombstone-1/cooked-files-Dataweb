cooked files for Data server project with custom User models:

points to note:
1. when you change from default django User models to custom User , will receive an error ----

        "django.db.migrations.exceptions.InconsistentMigrationHistory: "

it comes cause your database has already a django default user model migrate may be cause of first migration. In that case :
    
   1. if you don't have any thing important on your DB just delete it.
    2. but if you do have just go an comment
            settings.py  ---  "django.contrib.admin"
            urls.py --- path(admin/)

this will solve issue.

2. not uploading db(too big) waste of space. so as soon as you get files first do migrations both account and main app.

3. create super user won't run on this so make superuser either from django admin or just register on site.