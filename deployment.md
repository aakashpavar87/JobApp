<h1>Step For Deploying Django Project</h1>

- 1. create Procfile in root of project
   copy paste below code
        - web: gunicorn [JobApp, (your app name)]:wsgi --log-file -
- 2. create runtime.txt and put python version in that file
- 3. create requirements.txt and put all dependenscies of your project in that file
    - Execute this command for the same
        - python -m pip freeze > requirements.txt
