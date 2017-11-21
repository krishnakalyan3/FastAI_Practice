#/usr/bin/env bash

rsync -avz -e "ssh -i aws.pem" ubuntu@34.229.133.115:/home/ubuntu/FastAI_Practice/scripts/output/submission_101.csv .
