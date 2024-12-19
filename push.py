#!/usr/bin/env python3
# This script is used to push the pycsep docker image to dockerhub
# User must be logged into dockerhub and have write permissions to sceccode
#

import os
import datetime

cmd = "docker push sceccode/pycsep_quakeworx_workshop"
print("Running: ", cmd)
os.system(cmd)
