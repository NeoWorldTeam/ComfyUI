#!/bin/bash

# 下载文件
cg down nahz202/InstantID_Mo/ip-adapter.bin
cg down nahz202/InstantID_Mo/diffusion_pytorch_model.safetensors
cg down nahz202/InstantID_Mo/antelopev2.zip

# 移动文件
mv InstantID_Mo/ip-adapter.bin models/instantid/
mv InstantID_Mo/antelopev2.zip models/antelopev2/
mv InstantID_Mo/diffusion_pytorch_model.safetensors models/controlnet/instantid/

# 解压缩antelopev2.zip
unzip models/antelopev2/antelopev2.zip -d models/antelopev2/

pip install insightface kornia
pip uninstall onnxruntime onnxruntime-gpu
pip install nvidia-pyindex
pip install onnxruntime
pip install onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/
pip install onnx-graphsurgeon
