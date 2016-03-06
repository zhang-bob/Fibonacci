# Fibonacci
A REST API to return Fibonacci string 

1. How to deploy this script:
    Copy the folder into a proper location in your website
    Import the package fibonacci in urls.py of main web service folder
    add following lines in urlpatterns, it will be enable on web server
    #######################################
    from fibonacci import views
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('fibonacci.urls')),
    ]
    ########################################

2. How to run the script
    send http request to your webservice director:
    
    http <service service IP>/fibonacci/<integer>

    integer number here is the length of fibonacci array you want to query

3. How to test it
    all test cases are in Test suite, it's easy to run TestSuite.py for the test:
    python TestSuite.py

4. for any issues, please send email to me
    xh1158@sina.com

