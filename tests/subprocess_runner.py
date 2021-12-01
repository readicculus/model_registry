#      This file is part of the PEP GUI detection pipeline batch running tool
#      Copyright (C) 2021 Yuval Boss yuval@uw.edu
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
from typing import Dict



def get_pipeline_cmd(debug=False, kwiver_setup_path = None):
    if os.name == 'nt':
        if kwiver_setup_path:
            return [f'"{kwiver_setup_path}"', '&&', 'kwiver.exe', 'runner']
        else:
            return ['kwiver.exe', 'runner']
    else:
        if debug:
            args = ['gdb', '--args', 'kwiver', 'runner']
        else:
            args = ['kwiver', 'runner']

        if kwiver_setup_path:
            args = ['source', kwiver_setup_path, '&&', 'printenv', '&&'] + args
        return args

def execute_command(cmd: str, env: Dict, cwd, stdout=None, stderr=None):
    if os.name == 'nt':
        env = {**env, **os.environ}
        return subprocess.Popen(cmd, cwd=cwd,  stdout=stdout, stderr=subprocess.STDOUT, env=env)
    else:
        env = {**env, **os.environ}
        return subprocess.Popen(cmd, cwd=cwd, stdout=stdout, stderr=stderr, env= env,  shell=True, executable='/bin/bash')


class KwiverRunner:
    '''
        Runner for running non-embedded pipelines that have no input output ports.
        Uses subprocess to call kwiver_runner
    '''
    def __init__(self, pipeline_fp, env, cwd, kwiver_setup_path=None, pipe_args = {}):
        self.pipeline_fp = pipeline_fp
        self.env = env
        self.cwd = cwd
        self.kwiver_setup_path = kwiver_setup_path
        self.pipe_args = pipe_args

    def get_windows_args_str(self):
        args_str = ""
        for k, v in self.pipe_args.items():
            args_str += '-s %s=%s ' % (k, v)
        return args_str

    def get_linux_args_str(self):
        args_str = ""
        for k, v in self.pipe_args.items():
            args_str += '-s %s=%s ' % (k, v)
        return args_str

    def get_windows_env_str(self):
        env_str = ""
        for k, v in self.env.items():
            env_str += 'SET %s=%s & ' % (k, v) + env_str
        env_str = env_str[:-2]
        return env_str

    def get_linux_env_str(self):
        env_str = ""
        for k, v in self.env.items():
            env_str += '%s=%s ' % (k, v) + env_str
        return env_str

    def run(self, stdout, stderr) -> subprocess.Popen:
        cmd = get_pipeline_cmd(kwiver_setup_path=self.kwiver_setup_path) + [self.pipeline_fp]
        cmd = ' '.join(cmd)
        if os.name == 'nt':
            env_str = self.get_windows_env_str()
            print(cmd.replace('&&', '&& ' + env_str))
        else:
            env_str = self.get_linux_env_str()
            print(cmd.replace('&&', '&& ' + env_str) )

        if os.name == 'nt':
            cmd += " " + self.get_windows_args_str()
        else:
            cmd += " " + self.get_linux_args_str()

        proc = execute_command(cmd, self.env, self.cwd, stdout=stdout, stderr=stderr)
        return proc



