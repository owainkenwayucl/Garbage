# Installing JAX on Mandelbrot/Fibonacci

There is an experimental port of JAX to IPU here (https://github.com/graphcore-research/jax-experimental). Unfortunately, it is experimental and this means it needs python 3.8 (we have 3.9) and Ubuntu (we are on RHEL).  This means the wheel for JAX works (as it's just python) but the wheel for JAXlib doesn't.

## Prerequisits:

1. Install Bazel 5.2.0 in the usual painful way and add to path.

```
git clone https://github.com/graphcore-research/jax-experimental
git clone https://github.com/graphcore-research/tensorflow-jax-experimental

source scl_source enable gcc-toolset-9
source /opt/graphcore/poplar_sdk-3.2.0/poplar-rhel_8-3.2.0+2580-b82480c629/enable.sh
source /opt/graphcore/poplar_sdk-3.2.0/popart-rhel_8-3.2.0+2580-b82480c629/enable.sh

export TF_POPLAR_BASE=/opt/graphcore/poplar_sdk-3.2.0/poplar-rhel_8-3.2.0+2580-b82480c629
```


```
virtualenv jax_build
source jax_build/bin/activate

pip install numpy==1.22.4 scipy cython pytest
```

go into the jax-experimental repo

```
git checkout jax-v0.3.15-ipu
```

Yes really - v0.3.16-ipu doesn't let you build O_o

```
build/build.py --enable_ipu --bazel_options=--override_repository=org_tensorflow=/PATH/TO/tensorflow-jax-experimental
```

(replace /PATH/TO/ with the absolute path)

You should end up with a wheel in `dist/jaxlib-0.3.15+ipu.sdk320-cp39-none-manylinux2014_x86_64.whl`

Pip Install that and the JAX one from the website (https://github.com/graphcore-research/jax-experimental/releases/download/jax-v0.3.16-ipu-beta2-sdk3/jax-0.3.16%2Bipu-py3-none-any.whl).

```python
from functools import partial
import jax
import numpy as np

@partial(jax.jit, backend="ipu")
def ipu_function(data):
    return data**2 + 1

data = np.array([1, -2, 3], np.float32)
output = ipu_function(data)
print(output, output.device())
```

```
(jax_build) [uccaoke@mandelbrot JAX]$ python3 test.py 
[ 2.  5. 10.] IpuDevice(id=0, num_tiles=1472, version=ipu2)
(jax_build) [uccaoke@mandelbrot JAX]$ 
```
