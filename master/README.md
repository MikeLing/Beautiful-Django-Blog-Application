<h1> Django Blogging App</h1><br>
<p>This is an example of django blogging app. Django provides a very fast and robust platform to build apps. As Django was invented to meet fast-moving newsroom deadlines, while satisfying the tough requirements of experienced Web developers. 

<h2>Pre Requirements </h2><br>

$ sudo apt-get install python3<br>
$ sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py <br>
$ sudo python get-pip.py<br>

<h2>Post Requirements</h2><br>
$ sudo git clone https://github.com/bharatkaistha/Beautiful-Django-Blog-Application.git<br>
<p>Clone the repository.</p><br>
$ cd Beautiful-Django-Blog-Application<br>
$ sudo pip install -r requirements.txt<br>
<p>This will install all the dependencies which are required for the installation of the app</p>

<h2> Setting Database</h2><br>

$ python3 manage.py makemigrations<br>
$ sudo python3 manage.py migrate<br>
$ sudo python3 manage.py runserver<br>

<h2>Host address</h2><br>
http://127.0.0.1:8000<br>
http://127.0.0.1:8000/blog/<br>
http://127.0.0.1:8000/admin/<br>
