import server
from aiohttp import web
import os
import json


dir = os.path.abspath(os.path.join(__file__, f"{os.getcwd()}/custom_nodes/neo_custom_node/resource/luban_project/json_data/styles"))
if not os.path.exists(dir):
    os.mkdir(dir)


def getStyles(request):
    if "name" in request.rel_url.query:
        name = request.rel_url.query["name"]
        file = os.path.join(dir, name+'.json')
        zhFile = os.path.join(dir, 'zh_CN.json')
        if os.path.isfile(zhFile):
            f = open(zhFile,'r', encoding='utf-8')
            zhData = json.load(f)
            f.close()

        if os.path.isfile(file):
            f = open(file,'r', encoding='utf-8')
            data = json.load(f)
            f.close()
            if data:
                ndata=[]
                if zhData:
                    for d in data:
                        nd={}
                        name=d['name'].replace('-',' ')
                        words=name.split(' ')
                        key=' '.join(word.upper() if word.lower() in ['mre','sai','3d'] else word.capitalize() for word in words)
                        nd['zhName']=zhData[key] if key in zhData else key
                        nd["name"]=d['name']
                        ndata.append(nd)
                return web.json_response(ndata)
    return web.Response(status=404)

class StyleSelecto:
    """
    提示词选择工具
    """
    def __init__(self):
        dir = os.path.abspath(os.path.join(__file__,f"{os.getcwd()}/custom_nodes/neo_custom_node/resource/luban_project/json_data/styles"))
        if not os.path.exists(dir):
            os.mkdir(dir)
        self.styleAll={}
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".json") and file.split(".")[0].find("styles")!=-1:
                    f = open(os.path.join(root, file), 'r', encoding='utf-8')
                    data = json.load(f)
                    f.close()
                    for d in data:
                        self.styleAll[d['name']] = d
    
    @classmethod
    def INPUT_TYPES(self):
        dir = os.path.abspath(os.path.join(__file__, f"{os.getcwd()}/custom_nodes/neo_custom_node/resource/luban_project/json_datastyles"))
        #获取目录全部yml文件名
        files_name=[]
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".json") and file.split(".")[0].find("styles")!=-1:
                    files_name.append(file.split(".")[0])

        return {
            "required": {
                "prompt": ("STRING", {"forceInput": True}),
                "style_type":(files_name, ),

            },
            "optional": {
                "negative_prompt":("STRING",{"forceInput": True}),
            },
            "hidden": {"unique_id": "UNIQUE_ID","wprompt":"PROMPT"},
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("正向提示词","反向提示词",)

    FUNCTION = "get_style"

    #OUTPUT_NODE = False

    CATEGORY = "Neo nodes/local"

    def get_style(self,prompt,style_type,unique_id,wprompt,negative_prompt=""):
        values = []
        if unique_id in wprompt:
            if wprompt[unique_id]["inputs"]['button']:
                #分割字符串
                values = wprompt[unique_id]["inputs"]['button'].split(',')
        for val in values:
            if 'prompt' in self.styleAll[val]:
                prompt=self.styleAll[val]['prompt'].format(prompt=prompt)
            if 'negative_prompt' in self.styleAll[val]:
                negative_prompt+=','+self.styleAll[val]['negative_prompt']

        return (prompt,negative_prompt)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "StyleSelecto": StyleSelecto
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "StyleSelecto": "风格选择器"
}
