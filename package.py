import os
import vdist.builder as builder
from vdist.configuration import Configuration
from vdist.source import directory

app = 'thebideo-comments'
project_dir = os.getcwd()
root_dir, tmp = os.path.split(project_dir)
ln_dir = root_dir + '/' + app
os.symlink(project_dir, ln_dir, True)

builder_parameters = {
            "app": app,
            "version": '1.0',
            "source": directory(path=ln_dir),
            "profile": 'centos7',
            "python_version": '3.6.6',
            "requirements_path": '/requirements.txt',
        }

configuration = Configuration(builder_parameters)

builder.build_package(configuration)
