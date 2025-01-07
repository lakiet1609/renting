from utils.common import read_yaml_file

class SysConfig:
    sys_cfg = read_yaml_file('./configs/config.yaml')
    data_file = sys_cfg['data_file']