from aip import AipSpeech
import os
import natsort

APP_ID = 'your appid'
API_KEY = 'your api_key'
SECRET_KEY = 'your secret_key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_file_name(dirPath):
    return os.walk(dirPath)


def write_to_file(file_path, write_str):
    with open(file_path, "a+") as file:
        file.write(write_str)


if __name__ == '__main__':
    path = os.path.abspath('.')
    path = os.path.join('source')
    with open("resultString.txt", "w") as file:
        file.write("")

    files = natsort.natsorted(os.listdir(path))

    for file in files:
        print('current file : ' + file)
        filePath = os.getcwd()
        filePath += '\\source\\' + file
        json = client.asr(get_file_content(filePath), 'wav', 16000, {
            'dev_pid': 1537,
        })
        if json['err_msg'] != "data empty.":
            resultStr = str(json['result'][0]) + '\n\n'
            write_to_file("resultString.txt", resultStr)
            print("Speech success : " + resultStr)
        else:
            print('Speech failed : ' + file)
