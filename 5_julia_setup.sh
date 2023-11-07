 # 1. download the latest stable release at https://julialang.org/downloads/
cd ~ 
 wget https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.9.3-linux-x86_64.tar.gz

 # 2. use tar to decompress
 tar xvzf ./julia-1.9.3-linux-x86_64.tar.gz

 # 3. add to PATH
 echo 'export PATH="$PATH:/home/ter066/julia.1.9.3/bin"' >> ~/.zshrc

# 4. install packages as needed, for example:
julia -e 'using Pkg; Pkg.add(["DataFrames", "Plots", "Statistics", "Distributed"])'

# list of previously used pacakges below:
# ArchGDAL
# ArgParse
# CSV
# Colors
# CovarianceMatrices
# DataFrames
# Distances
# GLM
# GR
# GeoArrays
# GeoData
# Glob
# HMMBase
# IJulia
# ImageView
# Images
# JSON
# LinearRegression
# NearestNeighbors
# OrderedCollections
# Plots
# PyCall
# PyPlot
# StaticArrays
# StatsBase
# TFRecord
# VegaLite
# Dates
# Distributed
# Printf
# Statistics
