import time
import os
import sys

from docker import Client


# looking for the container id
with open('/proc/self/cgroup') as f:
    lines = f.read().split('\n')

CID = lines[0].split('/')[-1]

print('Container ID: %s' % CID)

if not os.path.exists('/var/run/docker.sock'):
    print('Cannot see the Docker socket file, aborting')
    sys.exit(-1)
else:
    print('Docker sock file present.')


#RUN export EC2_AVAIL_ZONE=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
#RUN export EC2_REGION="`echo \"$EC2_AVAIL_ZONE\" | sed -e 's:\([0-9][0-9]*\)[a-z]*\$:\\1:'`"
#RUN export EC2_INSTANCE_ID=`curl -s http://169.254.169.254/latest/meta-data/instance-id`


def get_containers():
    cli = Client(base_url='unix://var/run/docker.sock')
    cli.containers()
    return [cont for cont in cli.containers() if cont['Id'] != CID]


def terminate_box():
    #aws ec2 terminate-instances --instance-ids $EC2_INSTANCE_ID --region $EC2_REGION
    pass


print('Watching')

while True:
    print(get_containers())
    time.sleep(1)

