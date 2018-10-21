import vdist.builder as builder
from vdist.configuration import Configuration
from vdist.source import directory

builder_parameters = {
            "app": 'thebideo-comments',
            "version": '1.0',
            "source": directory(path='C:\\Users\\nthor\source\\thebideo-comments'),
            "profile": 'centos7'
        }

configuration = Configuration(builder_parameters)

builder.build_package(configuration)
