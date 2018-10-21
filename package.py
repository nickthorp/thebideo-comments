import os
import vdist.builder as builder
from vdist.configuration import Configuration
from vdist.source import directory

project_dir = os.getcwd()

builder_parameters = {
            "app": 'thebideo-comments',
            "version": '1.0',
            "source": directory(path=project_dir),
            "profile": 'centos7'
        }

configuration = Configuration(builder_parameters)

builder.build_package(configuration)
