#!/usr/bin/python3
import yaml

gitDumpFile = "gitDump.yaml"
format_str = "git clone --branch {version} {url}"

with open('mur_init.sh', 'w') as output:
    output.write('#!/bin/bash\n')
    with open(gitDumpFile, 'r') as stream:
        repos = yaml.safe_load(stream)["repositories"]

        for repo in repos.values():
            output.write(format_str.format(**repo))
            output.write('\n')