
from commands.acceleration import acceleration
from commands.close_connection import close
from commands.distance import distance
from commands.send_time import send_time
from commands.test_command import test_command
from utils.error_handling import not_implemented


def get_command(command_str):

    if command_str == "test":
        return test_command
    elif command_str == "acceleration":
        return acceleration
    elif command_str == "close":
        return close
    elif command_str == "distance":
        return distance
    elif command_str == "time":
        return send_time
    
    else:
        return not_implemented(command_str)
    
