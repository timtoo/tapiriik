from .service_base import *
from .api import *

import tapiriik.local_settings as local_settings

# service name and corresponding local_settings.py identifier,
service_keys = {
    'Aerobia': '',
    'BeginnerTriathlete': 'BT_APIKEY',
    'Dropbox': 'DROPBOX_APP_KEY',
    'Endomondo': 'ENDOMONDO_CLIENT_KEY',
    'GarminConnect': '',
    'Motivato': 'MOTIVATO_PREMIUM_USERS_LIST_URL',
    'NikePlus': 'NIKEPLUS_CLIENT_ID',
    'Pulsstory': 'PULSSTORY_CLIENT_ID',
    'RideWithGPS': 'RWGPS_APIKEY',
    'RunKeeper': 'RUNKEEPER_CLIENT_ID',
    'Setio': 'SETIO_CLIENT_ID',
    'Singletracker': 'SINGLETRACKER_CLIENT_ID',
    'Smashrun': 'SMASHRUN_CLIENT_ID',
    'SportTracks': 'SPORTTRACKS_CLIENT_ID',
    'Strava': 'STRAVA_CLIENT_ID',
    'TrainAsONE': 'TRAINASONE_CLIENT_ID',
    'TrainerRoad': '',
    'TrainingPeaks': 'TRAININGPEAKS_CLIENT_ID',
    'VeloHero': '',
}

GLOBALS = globals()
for service_name in service_keys.keys():

    # upper case service name in local_settings is checked for 'ignore' first
    key = getattr(local_settings, service_name.upper(), None) or getattr(local_settings, service_keys[service_name], None)

    # lonly import non-ignored services that have local_settings non-default setting.
    if key == 'ignore' or key == '####' or key == 'http://...':
        GLOBALS[service_name] = None
    else:
        tmp = __import__('tapiriik.services.'+service_name, GLOBALS, locals(), [service_name+'Service'], 0)
        GLOBALS[service_name]= getattr(tmp, service_name+'Service')()


PRIVATE_SERVICES = []
try:
    from private.tapiriik.services import *
except ImportError:
    pass

from .service import *
from .service_record import *
