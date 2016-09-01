import random as rd
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import rpy2


def random_date(start='03/01/2009 12:00 AM', end='04/01/2009 12:00 AM'):
    """
    Modified from http://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    This function will return a random datetime between two datetime
    objects."""

    start = datetime.strptime(start, '%m/%d/%Y %I:%M %p')
    end = datetime.strptime(end, '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = rd.randrange(int_delta)
    return start + timedelta(seconds=random_second)
