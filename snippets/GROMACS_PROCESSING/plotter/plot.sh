#!/usr/bin/env bash

module load julia
julia -e "using Pkg; Pkg.activate(\"${PWD}\"); include(\"plot.jl\")"
