import os
import vdist.builder as builder
from vdist.configuration import Configuration
from vdist.source import directory

project_dir = os.getcwd()

builder_parameters = {
            "app": 'thebideo-comments',
            "version": '1.0',
            "source": directory(path=project_dir),
            "profile": 'ubuntu-trusty',
            "python_version": '3.6.6',
            "output_folder": '/tmp/vdist/'
        }

configuration = Configuration(builder_parameters)

builder.build_package(configuration)
