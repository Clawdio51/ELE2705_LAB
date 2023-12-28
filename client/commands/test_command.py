from utils.status_codes import STATUS_CODE

def test_command(config):
    
    data = "Test command executed."
    print(data)

    return {"status": STATUS_CODE.OK, "data": data}
    
