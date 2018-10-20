from vdist.builder import Builder
from vdist.source import directory

builder = Builder()

builder.add_build(
    app='thebideo-comments',
    version='1.0',
    source=directory(
        path='C:\\Users\\nthor\source\\thebideo-comments'
    ),
    profile='centos7',
    build_deps=['python', 'gcc'],
)

builder.build()
