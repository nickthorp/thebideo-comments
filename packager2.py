import os

from vdist.builder import Builder
from vdist.source import directory

project_dir = os.getcwd()
builder = Builder()

builder.add_build(
    app='thebideo-comments',
    source=directory(path=project_dir),
    version='1.0',
    profile='centos7',
    python_version='3.6.6',
)

builder.run_build()
