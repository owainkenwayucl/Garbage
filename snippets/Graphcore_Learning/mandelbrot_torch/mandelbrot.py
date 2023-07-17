import torch
import poptorch
import time
import sys
import numpy
import termshow # note this is the version from the Fractals repo that does numpy arrays :)

# functions to convert numbers into float32 tensors for IPU
def ipu_float(x):
    return ipu_float_([x])

def ipu_float_(x):
    return torch.tensor(x, dtype=torch.float32, device="ipu")

def ipu_int(x):
    return ipu_int_([x])

def ipu_int_(x):
    return torch.tensor([x], dtype=torch.int32, device="ipu")

# Define our "model"
class mandel_model(torch.nn.Module):
    def forward(self, cx, cy, zx, zy, k, n):
        zx2 = zx**2
        zy2 = zy**2
        infinite = (zx2 + zy2) > 4
        k[infinite] = n
        zx1 = zx2 - zy2 + cx
        zy1 = 2 * zx * zy + cy
        zx = zx1
        zy = zy1

        return zx,zy,k

# Main method
def generate_mandelbrot(xmin=-2.0, xmax=1.0, ymin=-1.0, ymax=1.0, xres=120, yres=41, n=25):
    print(f"Generate Mandelbrot with:\n  Space: x: {xmin}->{xmax}\n         y: {ymin}->{ymax}\n  Resolution: {xres}x{yres}x{n}\n")

    start = time.time()
    model = mandel_model()
    inference_model = poptorch.inferenceModel(model)

    x = torch.linspace(xmin, xmax, steps=xres, dtype=torch.float32)
    y = torch.linspace(ymin, ymax, steps=yres, dtype=torch.float32)

    xs, ys = torch.meshgrid(x, y, indexing="ij")
    w = xres
    h = yres
    zx = torch.zeros(w*h, dtype=torch.float32).reshape(w,h)
    zy = torch.zeros(w*h, dtype=torch.float32).reshape(w,h)
    k = torch.zeros(w*h, dtype=torch.int32).reshape(w,h)
    for i in range(n):
        zx,zy,k =inference_model(xs, ys, zx, zy, k,  torch.tensor([i], dtype=torch.int32))

    image = numpy.fliplr(k.numpy()/n)
    stop = time.time()
    return image

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="General Fractal Tool.")

# General options
    parser.add_argument("-W", "--width", metavar="width", type=int, help="Width.", default=120)
    parser.add_argument("-H", "--height", metavar="height", type=int, help="Height.", default=41)
    parser.add_argument("-x", "--xmin", metavar="xmin", type=float, help="Minimum value for X.", default=-2)
    parser.add_argument("-y", "--ymin", metavar="ymin", type=float, help="Minimum value for Y.", default=-1)
    parser.add_argument("-X", "--xmax", metavar="xmax", type=float, help="Maximum value for X.", default=1)
    parser.add_argument("-Y", "--ymax", metavar="ymax", type=float, help="Maximum value for Y.", default=1)
    parser.add_argument("-i", "--iters", metavar="iters", type=int, help="Maximum number of iterations.", default=25)
    args = parser.parse_args()

    image = generate_mandelbrot(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.iters)

    termshow.show(image)

