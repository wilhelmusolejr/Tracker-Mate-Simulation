import platform

def get_machine_id():
    system_info = platform.uname()
    unique_id = f"{system_info.system}-{system_info.node}-{system_info.machine}"
    return unique_id