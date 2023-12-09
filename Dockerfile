FROM rocker/verse

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

RUN Rscript -e "install.packages(c('tidyverse', 'ggplot2'))"
RUN Rscript -e "install.packages('umap')"
