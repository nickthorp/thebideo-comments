import os
import vdist.builder as builder
from vdist.configuration import Configuration
from vdist.source import directory

app = 'thebideo-comments'
version = '1.' + os.environ['BUILD_NUMBER']
python_ver = '3.6.6'

root_dir, tmp = os.path.split(os.getcwd())
ln_dir = root_dir + '/' + app
os.symlink(os.getcwd(), ln_dir, True)

builder_parameters = {
            "app": app,
            "version": version,
            "source": directory(path=ln_dir),
            "profile": 'centos7',
            "python_version": python_ver,
            "requirements_path": '/requirements.txt',
            "output_folder": './vdist',
            #"runtime_deps": ["libssl1.0.0","libssl-dev"],
        }

configuration = Configuration(builder_parameters)

builder.build_package(configuration)

os.unlink(ln_dir)
