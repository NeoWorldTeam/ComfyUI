class AspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aspect_ratio": (['704×1408 ∣ 1:2','704×1344 ∣ 11:21','768×1344 ∣ 4:7','768×1280 ∣ 3:5'
                                  ,'832×1216 ∣ 13:19','832×1152 ∣ 13:18','896×1152 ∣ 7:9','896×1088 ∣ 14:17'
                                  ,'960×1088 ∣ 15:17','960×1024 ∣ 15:16','1024×1024 ∣ 1:1','1024×960 ∣ 16:15'
                                  ,'1088×960 ∣ 17:15','1088×896 ∣ 17:14','1152×896 ∣ 9:7','1152×832 ∣ 18:13'
                                  ,'1216×832 ∣ 19:13','1280×768 ∣ 5:3','1344×768 ∣ 7:4','1344×704 ∣ 21:11'
                                  ,'1408×704 ∣ 2:1','1472×704 ∣ 23:11','1536×640 ∣ 12:5','1600×640 ∣ 5:2'
                                  ,'1664×576 ∣ 26:9','1728×576 ∣ 3:1'], {"default": "1152×896 ∣ 9:7"}),
                "width": ("INT", {"default": 0, "min": 0, "max": 99999}),
                "height": ("INT", {"default": 0, "min": 0, "max": 99999}),
            }
        }
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("宽","高",)
    FUNCTION = "aspect_ratio"

    CATEGORY = "Neo nodes/Arg"


    def aspect_ratio(self,aspect_ratio,width,height):
        #判断不为自定义，提前宽高
        if width==0 and height==0:
            aspect_ratio = aspect_ratio.split("∣")
            width = int(aspect_ratio[0].split("×")[0])
            height = int(aspect_ratio[0].split("×")[1])
        return (width,height,)


class NeoParam:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 0, "min": 0, "max": 99999}),
                "height": ("INT", {"default": 0, "min": 0, "max": 99999}),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "step": ("INT", {"default": 24, "min": 4, "max": 50}),
                "cfg": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 30}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 99999999999999}),
                "upscale": ("FLOAT", {"default": 1, "min": 1, "max": 4}),
            }
        }

    RETURN_TYPES = ("INT", "INT","STRING","STRING","INT","FLOAT","INT","FLOAT",)
    RETURN_NAMES = ("宽", "高","提示","负面提示","步长","cfg","种子","放大倍数",)
    FUNCTION = "params_out"

    CATEGORY = "Neo nodes/Arg"

    def params_out(self,width,height,prompt,negative_prompt,step,cfg,seed,upscale):
        return (width,height,prompt,negative_prompt,step,cfg,seed,upscale,)



NODE_CLASS_MAPPINGS = {
    "AspectRatio": AspectRatio,
    "NeoParam": NeoParam
}


# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatio": "宽高比",
    "NeoParam": "Neo参数"
}