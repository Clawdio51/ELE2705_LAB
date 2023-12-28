import time

from utils.status_codes import STATUS_CODE

def send_time(config):

    data = time.asctime(time.localtime(time.time()))
    print("Time sent.")

    return {"status": STATUS_CODE.OK, "data": data}
