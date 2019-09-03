import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--redis_password", default="password", type=str)
args = parser.parse_args()

print( "worker node -- cpu" )
os.system( "ray start --redis-address=10.1.0.5:6000 --redis-password='password'"