FROM rocker/r-ver:4.1.0

RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    libxml2-dev \
    libcurl4-openssl-dev \
    libssl-dev

RUN apt update && apt install -y python3-pip sqlite3
RUN pip3 install --upgrade pip
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install jupyter
RUN pip3 install jupyterlab
RUN pip3 install bokeh
RUN pip3 install jupyter_bokeh


RUN R -e "install.packages(c('tidyverse', 'ggplot2','umap', repos='https://cloud.r-project.org/')"

