from fabric.api import local
from datetime import datetime


def do_pack():
    time_test = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "/versions/web_static_" + time_test + ".tgz"
    command1 = "mkdir -p versions"
    command2 = "tar -czvf " + "." + file_name + " web_static"
    local(command1)
    com = local(command2)
    if com.return_code == 0:
        return (com)
    else:
        return None
