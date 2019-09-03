import os
import time
import argparse

import ray

parser = argparse.ArgumentParser()
parser.add_argument( "--redis_address", default="localhost", type=str )
parser.add_argument( "--redis_password", default="password", type=str )
args = parser.parse_args()

ray.init( redis_address = args.redis_address , redis_password = args.redis_password ) 

@ray.remote
def f():
    time.sleep( 0.01 )
    return ray.services.get_node_ip_address()

print( "starting addrs" )
n = 0
while ( n < 5 ):
    time.sleep ( 30 )
    n = len( set( ray.get( [f.remote() for _ in range( 1000 ) ] ) ) )
    print( "found->{}< nodes in cluster".format( n ) )


print( "addresses in cluster->{}<".format( set( ray.get( [f.remote() for _ in range( 1000 ) ] ) ) ) )