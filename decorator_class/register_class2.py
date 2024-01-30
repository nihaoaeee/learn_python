from decorator_class.register_class1 import register_class


@register_class
class MasterTaskConf(object):
    @classmethod
    def get_conf(cls):
        return "master_task_conf"
