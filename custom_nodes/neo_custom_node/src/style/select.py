
import json
import os

from custom_nodes.neo_custom_node.resource.luban_project.python_schema.schema import cfg_Tables



def loader(f):

    return json.load(
        open(f"{os.getcwd()}/custom_nodes/neo_custom_node/resource/luban_project/json_data/" + f + ".json", "r", encoding="utf-8")
    )


luban_tables = None


# 添加缓存装饰器
# @lru_cache(maxsize=1)
def get_luban() -> cfg_Tables:
    global luban_tables
    if luban_tables is None:
        luban_tables = cfg_Tables(loader)
    return luban_tables


def find_image_styles_by_text_style(text_style):
    lt = get_luban()
    image_styles = lt.TbStoryType.get(text_style).upgrade_to_item_id
    return image_styles


def get_style_prompts(style_name):
    lt = get_luban()
    style = lt.TbStyle.get(style_name)
    print(style.key)
    print(style.prompt, style.negative_prompt)
    try:
        return style.prompt, style.negative_prompt
    except AttributeError:
        print(f"style_name not found in luban{style_name}")
        style = lt.TbStyle.get("enhance")

        return style.prompt, style.negative_prompt


class SDXLPromptOnlyStyler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        styles = list(get_luban().TbStyle.getDataMap().keys())

        return {
            "required": {
                "text_positive": ("STRING", {"default": "", "multiline": True}),
                "text_negative": ("STRING", {"default": "", "multiline": True}),
                "image_style": ((styles),),

            },
        }

    RETURN_TYPES = ('STRING', 'STRING',)
    RETURN_NAMES = ('text_positive', 'text_negative',)
    FUNCTION = 'prompt_styler'
    CATEGORY = "Neo nodes/prompt"


    def prompt_styler(self, text_positive, text_negative, image_style):
        text_positive_styled, text_negative_styled = get_style_prompts(image_style)
        text_positive_styled = text_positive_styled.replace("{prompt}", text_positive)
        text_negative_styled = text_negative + text_negative_styled
        print(text_positive_styled, text_negative_styled)
        return text_positive_styled, text_negative_styled

class SDXLStoryPromptStyler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        styles = list(get_luban().TbStoryType.getDataMap().keys())

        return {
            "required": {
                "text_positive": ("STRING", {"default": "", "multiline": True}),
                "text_negative": ("STRING", {"default": "", "multiline": True}),
                "story_style": ((styles),),
                "log_prompt": ("BOOLEAN", {"default": True, "label_on": "yes", "label_off": "no"}),
            },
        }

    RETURN_TYPES = ('STRING', 'STRING',)
    RETURN_NAMES = ('text_positive', 'text_negative',)
    FUNCTION = 'prompt_styler'
    CATEGORY = 'Neo nodes/prompt'

    def prompt_styler(self, text_positive, text_negative, story_style, log_prompt):
        styles = find_image_styles_by_text_style(story_style)
        all_prompt = ""
        for style in styles:
            p, np = get_style_prompts(style)
            all_prompt += p + ","
        text_positive_styled = all_prompt.replace("{prompt}", text_positive)
        text_negative_styled = text_negative + np


        # If logging is enabled (log_prompt is set to "Yes"),
        # print the style, positive and negative text, and positive and negative prompts to the console
        if log_prompt:
            print(f"style: {styles}")
            print(f"text_positive: {text_positive}")
            print(f"text_negative: {text_negative}")
            print(f"text_positive_styled: {text_positive_styled}")
            print(f"text_negative_styled: {text_negative_styled}")

        return text_positive_styled, text_negative_styled


NODE_CLASS_MAPPINGS = {
    "SDXLPromptOnlyStyler": SDXLPromptOnlyStyler,
    "SDXLStoryPromptStyler": SDXLStoryPromptStyler,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLPromptOnlyStyler": "SDXL Prompt Styler",
    "SDXLStoryPromptStyler": "SDXL Story Prompt Styler",
}