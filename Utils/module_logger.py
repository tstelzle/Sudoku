import os

LOGGING_DIRECTORY = 'logging/'


def create_logging_directory():
    if not os.path.exists(LOGGING_DIRECTORY):
        os.makedirs(LOGGING_DIRECTORY)
        os.chmod(LOGGING_DIRECTORY, 0o777)


def log_file_exists(file_name: str):
    if os.path.isfile(get_complete_file_name(file_name)):
        return True
    return False


def create_log_file(file_name: str):
    create_logging_directory()
    if not log_file_exists(file_name):
        os.mknod(get_complete_file_name(file_name))
        os.chmod(get_complete_file_name(file_name), 0o777)


def get_file_name_with_extension(file_name: str):
    return file_name + '.txt'


def get_complete_file_name(file_name: str):
    return LOGGING_DIRECTORY + file_name + '.txt'


def append_to_log(file_name: str, text: str):
    if not log_file_exists(file_name):
        create_log_file(file_name)
    log = open(get_complete_file_name(file_name), 'a')
    log.write(text)
    log.write("\n")
    log.close()
