source  /etc/proxy/net_proxy
# For CUDA Graph
export NEXFORT_FX_CUDAGRAPHS=1

# For best performance
export TORCHINDUCTOR_MAX_AUTOTUNE=1
# Enable CUDNN benchmark
export NEXFORT_FX_CONV_BENCHMARK=1
# Faster float32 matmul
export NEXFORT_FX_MATMUL_ALLOW_TF32=1

# For graph cache to speedup compilation
export TORCHINDUCTOR_FX_GRAPH_CACHE=1

# For persistent cache dir
export TORCHINDUCTOR_CACHE_DIR=~/.torchinductor



# debug
# export  TORCH_LOGS="+dynamo"
# export  TORCHDYNAMO_VERBOSE=1
# export NEXFORT_DEBUG=1 NEXFORT_FX_DUMP_GRAPH=1 TORCH_COMPILE_DEBUG=1

python main.py --cuda-device 0 --enable-cors-header --listen 0.0.0.0 --port 6006 --highvram --disable-cuda-malloc