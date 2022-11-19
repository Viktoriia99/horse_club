import os
import random
import math

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'horse_club_key'
    APP_NAME = os.environ.get('APP_NAME') or 'Horse Club Project'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql+psycopg2://' + \
                              'postgres:2418' + \
                              '@localhost:5432/HorseClub'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
