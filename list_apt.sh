#!/bin/bash
# Print apt-get history
# 2020-10-07    Include packages installed by packagekit
for logf in $(ls /var/log/apt/history.log.*.gz | sort -rV) ; do zcat $logf | grep -E -A 1 "Start-Date:|Commandline:" | sed -e '/Requested-By:/d' ; done
