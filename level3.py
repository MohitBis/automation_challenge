import argparse
import os
import time

# pip install google-api-python-client
import googleapiclient.discovery
from six.moves import input

compute = googleapiclient.discovery.build('compute', 'v1')

def deploy_instance(compute, project, zone, name, bucket):
    # Get the image.
    image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-9').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    config = {
        'name': name,
        'machineType': machine_type,

        # Disk
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # network
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }]
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()

deploy_instance(compute,'xyx' ,'abc', 'pyvm','pybucket')