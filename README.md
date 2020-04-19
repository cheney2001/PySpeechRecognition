# PySpeechRecognition

基于百度开放平台的批量语音文件识别


###### 百度开放平台
> 需要在百度开放平台注册账号并创建一个语音识别实例 ，绑定SpeechRecognition 中的对应参数

###### 详细baidu API 详见
> https://ai.baidu.com/ai-doc/SPEECH/tk4o0bm3v

#### 项目模块
> convertPCM将目录下文件转换为PCM格式 适合开放平台要求（提高识别率）
> DownloadMP3 批量下载mp3

-	SpeechRecognition
	- convertPCM 
	- main

-	DownloadMP3
	- main		

#### 使用教程
1. DownloadMP3 批量下载
	将URL逐行加入DownloadMP3/data.txt 即可
2. convertPCM 转换音频格式
	执行后输入需要转换的MP3文件所在目录，将转换目录下所有MP3文件为PCM格式生成的文件在源文件目录下
3. SpeechRecognition 批量识别PCM
	将需要识别转换好的PCM格式音频CP 到source 目录下 ，之后执行即可，识别好的语音将会逐行写入resultString.txt 文件中
