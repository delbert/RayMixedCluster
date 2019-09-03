import os
import time
import argparse

import ray

parser = argparse.ArgumentParser()
parser.add_argument( "--redis_address", default="localhost", type=str )
parser.add_argument( "--redis_password", default="password", type=str )
args = parser.parse_args()

ray.init( redis_address = args.redis_address , redis_password = args.redis_password ) 

while ( True ):
    time.sleep ( 33 )
    print( "in gpu node for cluster" )