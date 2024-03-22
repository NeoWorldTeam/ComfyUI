#!/bin/bash

# 下载文件
cg down nahz202/InstantID_Mo/ip-adapter.bin
cg down nahz202/InstantID_Mo/diffusion_pytorch_model.safetensors
cg down nahz202/InstantID_Mo/antelopev2.zip

# 移动文件
mv InstantID_Mo/ip-adapter.bin models/instantid/
mv InstantID_Mo/antelopev2.zip models/insightface/models/antelopev2/
mv InstantID_Mo/diffusion_pytorch_model.safetensors models/controlnet/instantid/

# 解压缩antelopev2.zip
unzip models/insightface/models/antelopev2/antelopev2.zip -d models/insightface/models/antelopev2/
