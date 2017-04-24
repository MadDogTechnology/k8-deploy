import logging
import datetime
from functools import partial
from os import environ as ENV
from copy import copy, deepcopy
from tags import get_docker_image_and_git_tag_version

def msg(name, status, arguments, error=""):
    tag = get_docker_image_and_git_tag_version()
    return "event-time-utc={time} task={name} status={status} arguments={arguments} environment={environment} git-tag={git_tag} docker-image-tag={docker_image_tag}, error={error}".format(
            time=datetime.datetime.utcnow(),
            name=name,
            status=status,
            arguments=arguments,
            environment=ENV["ENVIRONMENT"],
            git_tag=tag,
            docker_image_tag=tag,
            error=error
            )


def setup_log(func, messanger):
    def log_func_wrapper(*arguments, **keywords):
        messanger.info(msg(func.__name__, ENV["STARTED"], arguments))
        try:
            result = func(*arguments, **keywords)
            messanger.info(msg(func.__name__, ENV["COMPLETED"], arguments))
            return result
        except Exception as e:
            messanger.critical(msg(func.__name__, ENV["FAILED"], arguments, e.output))
            raise e
    return log_func_wrapper



def _log(log_func, log_mechnism): return partial(log_func, messanger=log_mechnism)

def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return _log(setup_log, logger)
