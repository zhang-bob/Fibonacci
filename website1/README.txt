==========================
How to deploy the script
==========================
The program is developed using django, so it's recommended to deploy the program under django's controll. First of all,
You need install dependent packages in order to make the program run

===========================
Step1: install dependent Python packages
============================
    the packages listed below should be installed in sequence
    1.1 django
    1.2 djangorestframework
    1.3 markdown
    1.4 django-filter
    1.5 pygments
    1.6 httpie

=============================
Step2: create your own project using Django
=============================
    After install Django, you can create a project in your working folder by following command:
        # django-admin-script.py startproject myproject
    Then you can see a folder myproject in current folder, then go into this folder

=============================
Step3: create a new application fibonacci under project myproject
=============================
    Run this command under myproject folder, it will create a folder named fibonacci
        #python manage.py startapp fibonacci

==============================
Step4: Copy source codes in fibonacci into the new created folder with same name
==============================
    copy source code into the folder
        # cp <source code in fibonacci>/* fibonacci/

=============================
Step5: Modify settings.py and urls.py in myproject folder
==============================
    5.1 add following code into myproject/settings.py
    #############################################################
    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }

    5.2 add 2 lines into INSTALLED_APPS array in settings.py
    'fibonacci',
    'rest_framework',

    5.3 add a entry to myproject/urls.py, to ensure source code can be called
    #######################################
    from fibonacci import views
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^', include('fibonacci.urls')),
    ]
    ########################################

==========================================
Step6: start server and try
===========================================
    Start web service by following command:
    # python manage.py runserver

    native this link: http://127.0.0.0.1:8000

============================================
Step7: Get fobonacci array
============================================
    navigate the link: http http://127.0.0.1:8000/fibonacci/<integer>

    the program will return a fibonacci array with <integer> length.

    positive number is only allowed, the maximum value is 5000. you can modify the maximum limitation by edit fibonacciArray.py
    in fibonacci folder.

===========================================
Step8: How to run regression test
===========================================
    run test suite in Test folder which contains necessary test cases, in order to avoid regression
    # Python TestSuite.py