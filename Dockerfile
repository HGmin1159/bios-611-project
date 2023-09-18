FROM rocker/verse
RUN apt update && apt install -y man-db manpages coreutils
RUN yes | unminimize
RUN rm -rf /var/lib/apt/lists/*

