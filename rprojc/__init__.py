import os

from rutils import ProjectWorker


class StandardProject(ProjectWorker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        homedir = self.config.get("PROJECT_HOME", ".")
        workdir = os.path.abspath(os.path.join(homedir, "workdir"))

        if not os.path.exists(workdir):
            os.makedirs(workdir)
            self.logger.info("Initialized workdir: {}".format(workdir))

        self.config["WORKDIR"] = workdir
