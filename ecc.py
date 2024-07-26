from cryptoauthlib import *
from cryptography.hazmat.primitives.asymmetric import ec

# Maps common name to the specific name used internally
atca_names_map = {'i2c': 'i2c', 'hid': 'kithid', 'sha': 'sha20x', 'ecc': 'eccx08'}
swarmkey_slot = 0
ATCA_SUCCESS = 0x00

class EccError(Exception):
    pass

def ecc_cfg():
    iface = "i2c"
    device = "ecc"
    cfg = eval('cfg_at{}a_{}_default()'.format(atca_names_map.get(device), atca_names_map.get(iface)))
    cfg.cfg.atcai2c.bus = 1
    res = atcab_init(cfg)
    if not ATCA_SUCCESS == res:
        raise EccError("Init ECC608 Error: {:d}".format(res))

if __name__ == '__main__':
    ecc_cfg()
