## venuebooking

### Introduction

venuebooking is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.



### Overview
In this app you can create  venues, artists and shows for them, in each artist you can see 
all the information about the artist besides the past and upcoming shows he will perform at,
and the same for venues too with the past and upcoming shows it will be hosted.

- creating new venues, artists and shows.
- modify venues and artists
- delete venues and artists
- list all venues, artists and shows
- searching for venues and artists.
- learning more about a specific artist or venue.

### Tech Stack

The tech stack for this project was:

- **PostgreSQL** as the database of choice
- **Python3** and **Django** as the server language and server framework
- **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for the website's frontend

### Main Files: Project Structure

```sh
├── README.md
├── manage.py 
├── venuebooking
    ├──── setting.py
    ├──── urls.py
    .
    .
    .

├── venues *** the venue  app
   ├──── templates
   ├──── models.py
   ├──── views.py
   .
   .
   .
├── artists *** the artist  app
   ├──── templates
   ├──── models.py
   ├──── views.py
   .
   .
   .
├── shows *** the show  app
   ├──── templates
   ├──── models.py
   ├──── views.py
   .
   .
   .
├── requirements.txt *** The dependencies to be installed with "pip3 install -r requirements.txt"
├── static
    ├── css
    ├── font
    ├── ico
    ├── img
    └── js
└── templates
    ├── errors
    ├── base.html
    └── home.html
```

### Development Setup

To start and run the local development server,

1. Initialize and activate a virtualenv:

```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

2. Install the dependencies:

```
$ pip install -r requirements.txt
```
3. Config your database settings in venuebooking/settings.py
    - set your dbname
    - set your db user
    - set your password

4. Run the development server:

```
$ python manage.py runserver
```

5. Navigate to Home page [http://localhost:800](http://localhost:800)