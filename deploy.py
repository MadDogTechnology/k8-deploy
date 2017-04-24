from csv import DictReader
from execute import execute
from os import environ as ENV
from log import log


def deploy_management(services):
    for service in services:
        execute(["kubectl", 
                    "set", "image",
                    "deployment/{deployment}".format(deployment=service["deployment"]),
                    "{image_ref}={image_val}".format(image_ref=service["image-ref"], image_val=service["image-val"])])


@log()
def deploy(deployment, image_ref, image_val):
    print(deployment, image_ref, image_val)

def from_csv(file_path):
    with open(file_path) as f:
        return list(DictReader(f))

@log()
def deploy_services_to_kubernetes():
    deploy_management(from_csv("services.csv"))

