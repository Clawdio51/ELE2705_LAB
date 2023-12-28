from utils.status_codes import STATUS_CODE

def close(config):
    
    data = "Connection Terminated."

    return {"status": STATUS_CODE.CLOSE, "data": data}