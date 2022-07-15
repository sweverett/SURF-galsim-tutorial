import yaml

def read_yaml(yaml_file):
    '''
    current package has a problem reading scientific notation as
    floats; see
    https://stackoverflow.com/questions/30458977/yaml-loads-5e-6-as-string-and-not-a-number
    '''

    loader = yaml.SafeLoader
    loader.add_implicit_resolver(
        u'tag:yaml.org,2002:float',
        re.compile(u'''^(?:
        [-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+]?[0-9]+)?
        |[-+]?(?:[0-9][0-9_]*)(?:[eE][-+]?[0-9]+)
        |\\.[0-9_]+(?:[eE][-+][0-9]+)?
        |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*
        |[-+]?\\.(?:inf|Inf|INF)
        |\\.(?:nan|NaN|NAN))$''', re.X),
        list(u'-+0123456789.'))

    with open(yaml_file, 'r') as stream:
        # return yaml.safe_load(stream) # see above issue
        return yaml.load(stream, Loader=loader)

def write_yaml(yaml_dict, yaml_outfile):
    with open(yaml_outfile, 'w') as yaml_file:
        yaml.dump(yaml_dict, yaml_file, default_flow_style=False)

    return
