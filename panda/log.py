import logging

def log(fn):
    logging.basicConfig(level="DEBUG")

    lg = logging.getLogger("mylogger")

    fl = logging.FileHandler(f'{fn}')
    fl.setLevel("DEBUG")
    lg.addHandler(fl)
    return lg

