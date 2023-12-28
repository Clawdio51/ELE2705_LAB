from utils.status_codes import STATUS_CODE

def not_implemented(command_str):
    
    data = f"Command {command_str} is not implemented."
    print(data)

    def f():
        return {"status": STATUS_CODE.UNDEFINED, "data": data}
    
    return f