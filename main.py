"""

这是一个基于 OpenAI GPT 文本生成模型的语音交互程序，可以将语音输入转换为文本，通过 OpenAI API 进行问答生成回答，然后将回答转换为语音输出。具体流程如下：

加载必要的模块和资源，如 pyttsx3 引擎、语音识别器、OpenAI API key、历史记录等。
定义一个生成回答的函数 generate_response，该函数接收一个问题，通过 OpenAI API 调用 GPT 模型生成回答。
定义一个获取机器人回答的函数 get_response，该函数先检查历史记录中是否有该问题的回答，如果有则直接返回，否则调用 generate_response 函数生成回答，并将问题和回答保存到历史记录中。
定义一个保存历史记录的函数 save_history，该函数将问题和回答保存到一个 JSON 文件中。
定义一个将文本转换为语音输出的函数 speak，该函数使用 pyttsx3 引擎将文本转换为语音并输出。
在主程序中，不断循环等待语音输入，将语音转换为文本后调用 get_response 函数获取机器人回答，并将回答转换为语音输出。当输入为 "stop" 时，退出程序。
"""
import json
import os
import pyttsx3
import speech_recognition as sr
import openai

# 我的chatgpt的api,如下载请别用这个api_key，请自己下一个新的
openai.api_key = "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"

# 加载历史记录
if os.path.isfile('history.json'):
    with open('history.json', 'r') as f:
        history = json.load(f)
else:
    history = {}


# 调用 OpenAI API 进行文本生成的函数
# 接收一个字符串 prompt 作为参数，用于提供生成文本的开头或者提示。
def generate_response(prompt):
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    message = completions.choices[0].text.strip()
    return message

# 保存历史记录
def save_history(prompt, response):
    if prompt not in history:
        history[prompt] = []
    history[prompt].append(response)
    with open('history.json', 'w') as f:
        json.dump(history, f)


# 获取机器人对于用户输入的回答，并将回答保存到历史记录中，如果历史记录中有对应的回答，则直接返回历史记录中的回答。
# 获得文字回答
def get_response(prompt):
    if prompt in history:
        print("正在读取之前的回答...")
        return history[prompt][-1]
    else:
        response = generate_response(prompt)
        print("机器人回答：", response)
        save_history(prompt, response)
        return response

# 文本转语音
def speak(text):
    # 初始化 pyttsx3 引擎
    engine = pyttsx3.init()

    # 获取语音识别器
    r = sr.Recognizer()

    # 获取所有支持的声音列表
    voices = engine.getProperty('voices')

    # 声音进行设置，我选择的是tingting的语音包
    zh_voice_id = "com.apple.speech.synthesis.voice.ting-ting"
    #ko_voice_id = "com.apple.speech.synthesis.voice.yuna"
    engine.setProperty('voice', zh_voice_id)
    engine.setProperty('volume', 0.5)
    engine.setProperty('rate', 200)

    # 用语音包ID来配置engine
    engine.setProperty('voice', zh_voice_id)
    engine.say(text)
    engine.runAndWait()

# 进行交互测试
while True:
    # 获取麦克风输入
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("请开始您的提问...")
        audio = r.listen(source)
    # 将语音转为文本
    try:
        #prompt = r.recognize_google(audio, language='ko-KR')
        prompt = r.recognize_google(audio, language='zh-CN')
        print("你说：", prompt, flush = True)

        if prompt == "stop" or prompt == "停止":
            break
        # 获取机器人的文字回答并打印出来
        response = get_response(prompt)
        # 将回答转换为语音
        speak(response)
    except sr.UnknownValueError:
        print("无法识别语音")
    except sr.RequestError as e:
        print("无法连接到API：{0}".format(e))
