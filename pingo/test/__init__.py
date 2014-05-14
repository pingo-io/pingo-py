import level0
import level1

def not_has_module(value):
    from pip.util import get_installed_distributions
    return (value not in [i.project_name for i in get_installed_distributions()])
