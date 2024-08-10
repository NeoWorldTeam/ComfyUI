export COMFYUI_ONEDIFF_SAVE_GRAPH_DIR="./graphs"
# Enable graph cache for faster compilation
export TORCHINDUCTOR_FX_GRAPH_CACHE=1
# For persistent cache dir
export TORCHINDUCTOR_CACHE_DIR=./torchcache
# debug
# export  TORCH_LOGS="+dynamo"
# export  TORCHDYNAMO_VERBOSE=1
# export NEXFORT_DEBUG=1 NEXFORT_FX_DUMP_GRAPH=1 TORCH_COMPILE_DEBUG=1
rm -rf ./output/*
python main.py --enable-cors-header --listen 0.0.0.0 --port 6006 --highvram --disable-cuda-malloc --use-pytorch-cross-attention