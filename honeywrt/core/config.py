import configparser, os

def config():
    cfg = configparser.ConfigParser()
    for f in ('honeywrt.cfg', '/etc/honeywrt/honeywrt.cfg', '/etc/honeywrt.cfg'):
        if os.path.exists(f):
            cfg.read(f)
            return cfg
    return None
