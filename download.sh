#!/usr/bin/env bash

wget http://files.fast.ai/data/aclImdb.tgz -P data
tar -xvzf data/aclImdb.tgz -C data/
rm data/aclImdb.tgz
