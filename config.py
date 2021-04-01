import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OBJECTS_PER_PAGE=3
<<<<<<< HEAD
    PATH_ABS=basedir
=======
>>>>>>> ea93205c0d654ed07215b6c6a639f6913685ce31
