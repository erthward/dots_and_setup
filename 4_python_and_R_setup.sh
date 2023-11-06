# (following instructions at https://docs.conda.io/projects/miniconda/en/latest/)

# create a directory for miniconda (the minimal conda installer)
mkdir -p ~/miniconda3

# download and run the installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# then remove the installer
rm -rf ~/miniconda3/miniconda.sh

# initialize the newly installed miniconda for both bash and zsh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# NOTE: IN A NEW TERMINAL WINDOW:
# prioritize the conda-forge channel and update existing packages to use it
conda config --add channels conda-forge
conda update -n base --all

# use conda to install mamba (because so much faster!)
conda install -n base mamba

# now create my general-purpose scientific working environment
mamba env create -f ~/dots_and_setup/conda/conda_environment.yml

# clean up tarballs
conda clean --all
