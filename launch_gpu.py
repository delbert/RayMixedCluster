import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "--redis_address", default="10.1.0.5:6000", type=str )
parser.add_argument( "--redis_password", default="password", type=str )
args = parser.parse_args()

print( "worker node -- gpu" )
os.system( "ray start --redis-address={} --redis-password='{}' --num-cpus=6 --num-gpus=1".format( args.redis_address , args.redis_password ) )
print( "sleeping" )
time.sleep ( 33 )
print( "waking up and running script" )
os.system( "python ray_cluster_gpu.py --redis_address={} --redis_password='{}'".format( args.redis_address , args.redis_password ) )