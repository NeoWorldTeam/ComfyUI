source  /etc/proxy/net_proxy
python main.py --cuda-device 0 --fp16-vae --fp16-unet --enable-cors-header --listen 0.0.0.0 --port 6006 --highvram --use-pytorch-cross-attention  --dont-upcast-attention