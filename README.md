# Shopping mall about product data with Python, MySQL and Django
This is my shopping website.
I used MySQL, which is not available in codio, so I had to install it in codio step by step, here is the installation tutorial (If you are using pycharm to open my application and you already have MySQL installed on your desktop, then you do not need to use the following installation steps to install MySQL in codio.): 

### Modify the database section in settings.py.
Install MySQL, and create a new scheme named 'product' in it, and correspond to the 'NAME': 'product', 'USER. root', 'PASSWORD', 'HOST: localhost', and 'PORT: 3306' as set in MySQL.
Modify the 'DATABASES' section in settings.py and change the password section to the password of your MySQL.

### Prerequisites
Ensure you are logged in as a user with sudo privileges.

### Installing MySQL on Codio (Ubuntu 18.04.4)
At the time of writing, the latest version of MySQL available in the Ubuntu repository is MySQL 8.0. To install it, run the following command:

    sudo apt update
    sudo apt install mysql-server
    
Once the installation is complete, the MySQL service will start automatically. To verify that the MySQL server is running, enter:

    sudo systemctl status mysql

The output should show that the service is enabled and running:

    ● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-05-05 14:14:22 UTC; 4min 2s ago
     Main PID: 8334 (mysqld)
     Tasks: 27 (limit: 153)
     
 ### Protecting MySQL
 The MySQL installation comes with a script called mysql_secure_installation which allows you to easily improve the security of your database server.
 To call the script without parameters:
 
     sudo mysql_secure_installation
     
 You will be asked to configure VALIDATE PASSWORD PLUGIN to test the strength of the MySQL user password and improve security with the following password:
     Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

    Securing the MySQL server deployment.
    
    Connecting to MySQL using a blank password.
    
    VALIDATE PASSWORD COMPONENT can be used to test passwords
    and improve security. It checks the strength of password
    and allows the users to set only those passwords which are
    secure enough. Would you like to setup VALIDATE PASSWORD component?

    Press y|Y for Yes, any other key for No: y
    
There are three levels of password verification policy: low, medium and strong. Press y if you want to set the authentication password plugin or any other key to move to the next step:
    
    There are three levels of password validation policy:

    LOW Length >= 8
    MEDIUM Length >= 8, numeric, mixed case, and special characters
    STRONG Length >= 8, numeric, mixed case, special characters and dictionary file

    Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 2
    
At the next prompt, you will be asked to set the password for the MySQL root user:

    Please set the password for root here.


    New password: 

    Re-enter new password: 
    
If you have set up the Verify Password plugin, the script will show you the strength of the new password. Type y to confirm the password:

    Estimated strength of the password: 50 
    Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y

Next, you will be asked to remove the anonymous user, restrict the root user's access to the local computer, delete the test database and reload the privilege tables. You should answer all questions.
    
    Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
    By default, a MySQL installation has an anonymous user,
    allowing anyone to log into MySQL without having to have
    a user account created for them. This is intended only for
    testing, and to make the installation go a bit smoother.
    You should remove them before moving into a production
    environment.
    
    Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
    Success.

    Normally, root should only be allowed to connect from
    'localhost'. This ensures that someone cannot guess at
    the root password from the network.

    Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
    Success.

    By default, MySQL comes with a database named 'test' that
    anyone can access. This is also intended only for testing,
     and should be removed before moving into a production
    environment.

    Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
     - Dropping test database...
    Success.

     - Removing privileges on test database...
    Success.

    Reloading the privilege tables will ensure that all changes
    made so far will take effect immediately.

    Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
    Success.

    All done! 

Enter the following code to display the contents of the debian.cnf file, which contains configuration information for the MySQL database server:
    
    sudo cat /etc/mysql/debian.cnf
    
Include this configuration information as follows:
    
    # Automatically generated for Debian scripts. DO NOT TOUCH!
    [client]
    host     = localhost
    user     = debian-sys-maint
    password = K4L1MVtWa5Az9GW7
    socket   = /var/run/mysqld/mysqld.sock
    [mysql_upgrade]
    host     = localhost
    user     = debian-sys-maint
    password = K4L1MVtWa5Az9GW7
    socket   = /var/run/mysqld/mysqld.sock
    
Below I have updated the password for the root user and set the authentication plugin to "mysql_native_password" for better security.

The "update user set plugin='mysql_native_password';" command updates the authentication plugin for all users to "mysql_native_password" instead of the default "auth_socket" on some Ubuntu systems. This change allows users to authenticate using the MySQL native password authentication method.

The "flush privileges;" command reloads the grant table, which tells the server to re-read the user account and privilege information stored in the system tables.

Finally, you exit the MySQL command line interface using the "exit" command.

### Logging in as root
Please note that these steps are important to secure your MySQL installation, but it is also important to take other security measures such as firewalls, regular backups and monitoring to ensure that your database is protected from unauthorised access and data loss.
To interact with MySQL Server from the command line, use the MySQL Client Utility, which is installed as a dependency of the MySQL Server software package.
    
    mysql -u debian-sys-maint -p
    
    
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 14
    Server version: 5.7.41-0ubuntu0.18.04.1 (Ubuntu)

    Copyright (c) 2000, 2023, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> use mysql
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A

    Database changed
    mysql> update mysql.user set authentication_string=password('Mbs600lzqy, ') where user='root' and Host='localhost';
    Query OK, 1 row affected, 1 warning (0.00 sec)
    Rows matched: 1  Changed: 1  Warnings: 1

    mysql> 
    mysql> update user set plugin='mysql_native_password';
    Query OK, 1 row affected (0.00 sec)
    Rows matched: 4  Changed: 1  Warnings: 0

    mysql> flush privileges;
    Query OK, 0 rows affected (0.00 sec)

    mysql> 
    mysql> exit
    Bye
    
The root user account has now been successfully used to log in to the MySQL command line interface after updating its password and authentication plug-in.
The "exit" command is used to terminate the MySQL command line interface session and return to the terminal prompt.

    mysql -u root -p
    
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 16
    Server version: 5.7.41-0ubuntu0.18.04.1 (Ubuntu)

    Copyright (c) 2000, 2023, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> exit
    Bye
    
To access the project:

    ls
    CS551Q_solo_assessment_April_2023.pdf  README.md  Shopping_QingyangZeng

    cd Shopping_QingyangZeng/
    ls
    
    cd sale/
    ls
    
    cd sale/

Open the settings.py file in the vim editor. To open the file in vim, you can type vim settings.py in the terminal.
Once the file is open in the vim editor, you can use various commands to edit the file. Here are some basic commands that you can use:

'i': to enter the insert mode (to start editing the file)
'Esc': to exit the insert mode (to go back to command mode)
':w': to save the changes made to the file
':q': to quit the editor
':q!': to force quit the editor without saving the changes
    
    cat settings.py 

Here are the outputs：
    
    """

    Django settings for sale project.

    Generated by 'django-admin startproject' using Django 3.2.2.

    For more information on this file, see
    https://docs.djangoproject.com/en/3.2/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/3.2/ref/settings/
    """
    import os
    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-fm(w8-!-b4d$o9d8gn1skf1_n0#0ji*=y&i%o@&z8l#5+to6$#'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "product",
        "user"
    ]
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'sale.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'sale.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'product', 
            'USER': 'root', 
            'PASSWORD': 'mbs600lzqy',
            'HOST': 'localhost', 
            'PORT': '3306', 
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'
    MEDIA_URL = "/upload/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    STATICFILES_DIRS = (os.path.join('static'), os.path.join('upload'),)codio@cleanfiesta-hunterdance:~/workspace/Shopping_QingyangZeng/sale/sale$ vim settings.py

A database named "product" has now been successfully created using the MySQL command line interface.
    
    mysql -u root -p 
    
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 20
    Server version: 5.7.41-0ubuntu0.18.04.1 (Ubuntu)

    Copyright (c) 2000, 2023, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> createdatabase product
        -> ;
    ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'createdatabase product' at line 1
    mysql> CREATE DATABASE  product;
    Query OK, 1 row affected (0.12 sec)

    mysql> exit
    Bye
    
The faker package was successfully installed using pip. When you run init_data.py, faker installs the package to fix the problem.
    
    pip install faker
    
    python3 manage.py makemigrations
    
    python3 manag.py migrate
    
    python3 init_data.py 

You will need to create a superuser as well if you want to work with the admin features. You can do that with the command:

    python3 manage.py createsuperuser

### Start the server
You only need to enter two directories, if not you can use the following
    
    cd Shopping_QingyangZeng
    cd sale

Three directories containing Shopping_QingyangZeng/sale/sale have been entered and can be used as follows:

    cd ..

The terminal should be cd'd in with the suffix '/Shopping_QingyangZeng/sale' before the following steps can be performed on the server.

We use the manage.py command tool by typing this command in the terminal:

    python3 manage.py runserver

If you are doing this on another platform, then you may need to change it (change the port number 8000 as required):

    python3 manage.py runserver 0.0.0.0:8000

### Search function
In the centre of the home page, there is a search function, which allows you to search by entering either or all of Productbrand and Productname, case sensitive. And when searching you can only click on SEARCH to find it, you can't use the enter key.

### Visualisation features

#### Map function
After finally starting the server, add 'statictics/', after the server website, to display a visualised world map. For example this is the website where my server can see the map: 'https://cleanfiesta-hunterdance-8000.codio-box.uk/statistics/'

#### Display icon function
Finally after starting the server, add 'area/' after the server website to display a visualised pie chart showing the distribution of the prices of the products. For example this is the website where my server can see the pie chart: 'https://cleanfiesta-hunterdance-8000.codio-box.uk/area/'

### Administrator functions
Add 'admin/' after the server URL. to show the backend administration. This is the website where my server can see the backend administrator: 'https://cleanfiesta-hunterdance-8000.codio-box.uk/admin/'

## If there is no '/' at the end of the URL, please add the '/' and enter the function you want to achieve e.g. 'admin', 'area', 'statistics'.

### Using tests
Here are also some basic tests so that you can see how to test whether your code is working properly. They are located in the "Tests" folder and cover model and view tests. There is some repetitive code to load the test database, which can be refactored into a separate file for test file calls. Use the following command to run the tests:

    python3 manage.py test
    
