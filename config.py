import os
class Config(object): 

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    #MONGODB_SETTINGS ={ 'db': 'UAT_commdeskcm'}