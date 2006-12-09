import os

class Constants:
    #PATHS
    #TAM_TAM_ROOT = os.getenv('TAMTAM_ROOT')
    TAM_TAM_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print 'INFO: loaded TAMTAM_ROOT=%s' % TAM_TAM_ROOT
    
    #DEFAULTS
    DEFAULT_TEMPO = 120
    DEFAULT_VOLUME = 0.8
    
    #NUMERICAL CONSTANTS
    NUMBER_OF_POSSIBLE_PITCHES = 25.0
    MINIMUM_PITCH = 24.0
    MAXIMUM_PITCH = MINIMUM_PITCH + NUMBER_OF_POSSIBLE_PITCHES - 1
    MINIMUM_NOTE_DURATION = 1 # ticks
    MS_PER_MINUTE = 60000.0
    TICKS_PER_BEAT = 12
    NUMBER_OF_TRACKS = 6
    NUMBER_OF_PAGES = 2

    MINIMUM_AMPLITUDE = 0
    MAXIMUM_AMPLITUDE = 1

    CSOUND_HORIZON = 0.100
    CLOCK_DELAY    = 0.04

