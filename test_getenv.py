'''
 5407  export TRANSFORMERS_VERBOSITY=error
 5408  echo $TRANSFORMERS_VERBOSITY
'''
import os
env_level_str = os.getenv("TRANSFORMERS_VERBOSITY", None)
print(env_level_str)

env_level_str = os.getenv("PATH", None)
print(env_level_str)

