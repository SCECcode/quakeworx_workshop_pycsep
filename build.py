#!/usr/bin/env python3
# This script is used to create a new docker container with pyCSEP
# This assigns the username as "csepuser" and assigns the image name as: pysep_quakeworx_workshop:latest

import os
import datetime

# build date tag
dt=datetime.datetime.today()
month=dt.month
day=dt.day
mdate="%02d%02d"%(month,day)


cmd = "docker build --progress=plain --no-cache=false -f Dockerfile . -t pycsep_quakeworx_workshop " \
"--build-arg APP_UNAME=csepuser --build-arg APP_GRPNAME=csepuser " \
"--build-arg APP_UID=1000 --build-arg APP_GID=1000 --build-arg BDATE=%s"%(mdate)
    
os.system(cmd)

cmd = "docker tag pycsep_quakeworx_workshop sceccode/pycsep_quakeworx_workshop"
print("Running: ",cmd)
os.system(cmd)

# To push image to dockerhub
# docker push sceccode/pycsep_quakeworx_workshop
