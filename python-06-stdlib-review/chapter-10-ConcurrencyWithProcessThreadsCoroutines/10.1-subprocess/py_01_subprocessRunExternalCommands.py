import sys, subprocess
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def subprocess_os_system():
    pass


if __name__ == "__main__":
    subprocess_os_system()