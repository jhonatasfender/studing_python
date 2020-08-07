FROM python:3.8

ENV HOME=/root

WORKDIR $HOME

RUN apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install -y --no-install-recommends \
  gnupg2 curl ca-certificates fonts-dejavu gfortran gcc wget git vim && \
  curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub | apt-key add - && \
  echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
  apt-get purge --autoremove -y curl \
  && rm -rf /var/lib/apt/lists/*

# for library pyautogui
# RUN apt-get isntall -y python3-tk scrot

# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN apt-get update && apt-get install -y --no-install-recommends \
  cuda-cudart-11-0=11.0.194-1 \
  cuda-compat-11-0 \
  && ln -s cuda-11.0 /usr/local/cuda && \
  rm -rf /var/lib/apt/lists/*

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
  echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility
ENV NVIDIA_REQUIRE_CUDA="cuda>=11.0 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441"
ENV CUDA_HOME=/usr/local/cuda

RUN python -m pip install pip jupyter notebook numba scrapy html5lib \
  bs4 numpy pandas scikit-learn tensorflow matplotlib seaborn \
  bokeh plotly pydot setuptools nb_black jupyterthemes PyAutoGUI \
  pandas-datareader

# https://github.com/dunovank/jupyter-themes
RUN jt -t chesterish

