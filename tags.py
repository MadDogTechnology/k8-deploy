from os import environ as ENV


def get_docker_image_and_git_tag_version():
    with open("git_and_docker_image_tag.txt", "r") as f:
        current_tag = f.read()
    if ENV["ENVIRONMENT"] != "local":
        return current_tag
    else:
        return "local"
