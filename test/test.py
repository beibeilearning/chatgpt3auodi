# 这段代码会把系统里的可用语音包的信息print出来
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)



# 把刚才代码输出的语音包ID信息储存起来
zh_voice_id = "com.apple.speech.synthesis.voice.ting-ting"

engine.say("hello")
# 用语音包ID来配置engine
engine.setProperty('voice', zh_voice_id)
engine.say("笑死了，你不是会说中文吗，为什么不说！！！气死我了！！！！！我差点要下载科大讯飞了！！！还差点要用百度api了")
engine.runAndWait()

"""
/Users/beibeizhang/.conda/envs/chatgpt/bin/python /Users/beibeizhang/PycharmProjects/chatgpt3/test.py
Voice:
 - ID: com.apple.speech.synthesis.voice.Alex
 - Name: Alex
 - Languages: ['en_US']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.alice
 - Name: Alice
 - Languages: ['it_IT']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.alva
 - Name: Alva
 - Languages: ['sv_SE']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.amelie
 - Name: Amelie
 - Languages: ['fr_CA']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.anna
 - Name: Anna
 - Languages: ['de_DE']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.carmit
 - Name: Carmit
 - Languages: ['he_IL']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.damayanti
 - Name: Damayanti
 - Languages: ['id_ID']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.daniel
 - Name: Daniel
 - Languages: ['en_GB']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.diego
 - Name: Diego
 - Languages: ['es_AR']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.ellen
 - Name: Ellen
 - Languages: ['nl_BE']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.fiona
 - Name: Fiona
 - Languages: ['en-scotland']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.Fred
 - Name: Fred
 - Languages: ['en_US']
 - Gender: VoiceGenderMale
 - Age: 30
Voice:
 - ID: com.apple.speech.synthesis.voice.ioana
 - Name: Ioana
 - Languages: ['ro_RO']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.joana
 - Name: Joana
 - Languages: ['pt_PT']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.jorge
 - Name: Jorge
 - Languages: ['es_ES']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.juan
 - Name: Juan
 - Languages: ['es_MX']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.kanya
 - Name: Kanya
 - Languages: ['th_TH']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.karen
 - Name: Karen
 - Languages: ['en_AU']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.kyoko
 - Name: Kyoko
 - Languages: ['ja_JP']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.laura
 - Name: Laura
 - Languages: ['sk_SK']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.lekha
 - Name: Lekha
 - Languages: ['hi_IN']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.luca
 - Name: Luca
 - Languages: ['it_IT']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.luciana
 - Name: Luciana
 - Languages: ['pt_BR']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.maged
 - Name: Maged
 - Languages: ['ar_SA']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.mariska
 - Name: Mariska
 - Languages: ['hu_HU']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.mei-jia
 - Name: Mei-Jia
 - Languages: ['zh_TW']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.melina
 - Name: Melina
 - Languages: ['el_GR']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.milena
 - Name: Milena
 - Languages: ['ru_RU']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.moira
 - Name: Moira
 - Languages: ['en_IE']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.monica
 - Name: Monica
 - Languages: ['es_ES']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.nora
 - Name: Nora
 - Languages: ['nb_NO']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.paulina
 - Name: Paulina
 - Languages: ['es_MX']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.rishi
 - Name: Rishi
 - Languages: ['en_IN']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.samantha
 - Name: Samantha
 - Languages: ['en_US']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.sara
 - Name: Sara
 - Languages: ['da_DK']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.satu
 - Name: Satu
 - Languages: ['fi_FI']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.sin-ji
 - Name: Sin-ji
 - Languages: ['zh_HK']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.tessa
 - Name: Tessa
 - Languages: ['en_ZA']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.thomas
 - Name: Thomas
 - Languages: ['fr_FR']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.ting-ting.premium
 - Name: Ting-Ting
 - Languages: ['zh_CN']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.veena
 - Name: Veena
 - Languages: ['en_IN']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.Victoria
 - Name: Victoria
 - Languages: ['en_US']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.xander
 - Name: Xander
 - Languages: ['nl_NL']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.yelda
 - Name: Yelda
 - Languages: ['tr_TR']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.yuna
 - Name: Yuna
 - Languages: ['ko_KR']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.yuri
 - Name: Yuri
 - Languages: ['ru_RU']
 - Gender: VoiceGenderMale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.zosia
 - Name: Zosia
 - Languages: ['pl_PL']
 - Gender: VoiceGenderFemale
 - Age: 35
Voice:
 - ID: com.apple.speech.synthesis.voice.zuzana
 - Name: Zuzana
 - Languages: ['cs_CZ']
 - Gender: VoiceGenderFemale
 - Age: 35

"""