from subprocess import CalledProcessError, check_output, STDOUT


def get_ram_usage():
    try:
        total_ram = int(
            str(check_output("cat /proc/meminfo | grep MemTotal |  grep -o '[0-9]*'", stderr=STDOUT, shell=True),
                encoding="utf-8")) / 1000
        free_ram = int(
            str(check_output("cat /proc/meminfo | grep MemFree |  grep -o '[0-9]*'", stderr=STDOUT, shell=True),
                encoding="utf-8")) / 1000
        ram_usage = {
            'total': "{0:.2f}".format(total_ram),
            'used': "{0:.2f}".format(total_ram - free_ram),
            'free': "{0:.2f}".format(free_ram),
            'used_p': "{0:.2f}".format((total_ram - free_ram) / total_ram * 100)
        }
        return ram_usage
    except CalledProcessError:
        return {
            'total': 'Proc Not Supported',
            'used': 'Proc Not Supported',
            'free': 'Proc Not Supported',
            'used_p': 'Proc Not Supported',
        }