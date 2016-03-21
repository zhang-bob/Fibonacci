# Fibonacci
A REST API to return Fibonacci string 

1. How to make web service running by django
    In order to make djanon web service running, you need install python packages described in requirements.txt at first. After that, you can start a project and application using django step by step
    1.1 Create a new project using any name you like
    # django-admin startproject PROJECT_NAME
    
    1.2 Go to this new project and then create a new application named fibonacci
    # cd PROJECT_NAME
    # python manage.py startapp fibonacci

    1.3 Copy all python scripts with postfix ".py" on git into fibonacci folder
    # cp -R *.py fibonacci


2. Associate new entry for application fibonacci 
    2.1 Make django aware the new application by editing settings file in folder PROJECT_NAME, add one lines in section "INSTALLED_APPS"
    ############################################
    INSTALLED_APPS = [
        'fibonacci',
    ]

    2.2 Add a URL entry for the application by editing urls.py in folder PROJECT_NAME: add 2 dependent package at the top of this file and then add a new url entry in section "urlpatterns"
    #############################################
    from fibonacci import views 
    .....
    urlpatterns = [
        url(r'^', include('fibonacci.urls')),
    ]

    2.3 Start web service by django
    # python manage.py runserver 


3. How to run the script
    send http request to your webservice directly:
    
    # http http://service service IP/fibonacci/INTEGER

    INTEGER number here is the length of fibonacci array you want to query. for example: 
    # http http://127.0.0.1:8000/fibonacci/50
    ["0 1 1 2 3 5 8 13 21 34"]


4. How to test it
    all test cases are in Test suite, it's easy to run TestSuite.py for the test:
    # python TestSuite.py


5. for any issues, please send email to me
    xh1158@sina.com

