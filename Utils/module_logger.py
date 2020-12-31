import os

LOGGING_DIRECTORY = 'logging/'


def initialize_logger():
    """
    Creates the directory, if not present, the directory to store the logs.
    :return: None
    """
    if not os.path.exists(LOGGING_DIRECTORY):
        os.makedirs(LOGGING_DIRECTORY)
        os.chmod(LOGGING_DIRECTORY, 0o777)


def log_file_exists(file_name: str):
    """
    Checks if the log file exists.
    :param file_name: file_name of the logfile
    :return: boolean
    """
    if os.path.isfile(get_complete_file_name(file_name)):
        return True
    return False


def create_log_file(file_name: str):
    """
    Creates a log file with the given name.
    :param file_name: file_name for the log
    :return: None
    """
    if not log_file_exists(file_name):
        os.mknod(get_complete_file_name(file_name))
        os.chmod(get_complete_file_name(file_name), 0o777)


def get_file_name_with_extension(file_name: str):
    """
    Returns the file_name with the format extension.
    :param file_name: file_name of the log
    :return: string
    """
    return file_name + '.txt'


def get_complete_file_name(file_name: str):
    """
    Returns the log file_name with the path of the logging directory
    :param file_name: file_name of the log
    :return: string
    """
    return LOGGING_DIRECTORY + file_name + '.txt'


def append_to_log(file_name: str, text: str):
    """
    Appends a text to the log file
    :param file_name: file_name of the log
    :param text: string which will be appended to the log
    :return: None
    """
    if not log_file_exists(file_name):
        create_log_file(file_name)
    log = open(get_complete_file_name(file_name), 'a')
    log.write(text)
    log.write("\n")
    log.close()
