
yum install gcc-c++ git -y
conda config --set always_yes true
conda config --add channels https://conda.anaconda.org/dranew
conda config --add channels https://conda.anaconda.org/shahcompbio
conda config --add channels 'bioconda'
conda install conda-build conda-verify anaconda-client
conda build conda/blossomv
anaconda -t $CONDA_UPLOAD_TOKEN upload /usr/local/conda-bld/linux-64/blossomv-*.tar.bz2


