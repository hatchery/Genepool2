from functools import wraps
import platform


operating_system = platform.system()
version = platform.mac_ver()[0]


def is_osx(versions=None):
    is_version = True
    if versions:
        is_version = version in versions
    return operating_system == 'Darwin' and is_version


def only_osx(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps
        def run_if_osx(*args, **kwargs):
            if is_osx(versions=versions):
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            else:
                # FiXME: should log and warn if warn
                pass

        return run_if_osx
    return wrapper