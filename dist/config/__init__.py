import configargparse

parser = configargparse.get_argument_parser(name='default')

parser.add_argument('--default-config', is_config_file=True,
                    default='./config/defaults.ini', help='default configuration file')

parser.add_argument('--user', type=str, help='Docker registry username', default='%(default)s')
parser.add_argument('--password', type=str, help='Docker registry password', default='%(default)s')
parser.add_argument('--catalog-url', type=str, help='Docker registry catalog url' )