import os
from rutils import ProjectWorker as _worker


class StandardProject(_worker):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            args = [self.get_classname()]
        if "proj_home" not in kwargs:
            kwargs["proj_home"] = os.path.abspath(".")
        super().__init__(*args, **kwargs)
        self.init()

    @classmethod
    def get_classname(cls):
        return cls.__name__

    def init(self):
        homedir = self.config.get("PROJ_HOME", ".")
        workdir = self.config.get(
            "WORKDIR", os.path.abspath(os.path.join(homedir, "workdir"))
        )

        if not os.path.exists(workdir):
            os.makedirs(workdir)
            self.logger.info("Initialized workdir: {}".format(workdir))

        self.config["WORKDIR"] = workdir
        if "PROJ_HOME" not in self.config:
            self.config["PROJ_HOME"] = workdir
