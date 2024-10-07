from typing import List

def countLetters(sentence: str) -> List[int]:
    letterCount: List[int] = [0] * 26 # 初始化一個長度為26的列表，對應著每個字母的計數

    for char in sentence: # 遍歷句子中的每個字母
        if char.isalpha(): # 檢查字符是否為字母
            index = ord(char) - ord('a') # 將字母轉換為對應索引(0-25)
            letterCount[index] += 1 # 增加對應字母的計數

    return letterCount # 返回字母計數列表
pass

def printLetterCount(letterCount: List[int]) -> None: # 遍歷字母計數列表

    for i in range(26): # 只打印計數大於0的字母
        if letterCount[i] > 0: #打印字母及其計數
            print(f"{chr(i + ord('a'))}: {letterCount[i]}")
pass

inputSentence: str = "this is an apple" # 定義輸入的句子
letterCount: List[int] = countLetters(inputSentence) # 計算字母的計數
printLetterCount(letterCount) # 打印字母計數