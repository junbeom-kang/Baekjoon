class Trie:
    head = {}

    def add(self, word):      #주어지는 단어를 Trie에 추가해주는 add함수
        cur = self.head       #cur을 맨위 head로 지정
        for ch in word:             #단어에 한 문자가 딕셔너리 자료형 cur에없다면 추가해준다
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]           #그리고 cur의 위치를 하위 노드로 바꿔준다

        # *가 있을 경우, 그 단어가 자료구조에 저장되어 있음을 의미
        # *가 없을 경우, 그 단어는 자료구조에 저장되어 있지 않음, 단지 더 긴 단어의 부분으로만 존재함
        cur['*'] = True            #마지막은 '*'를 사용하여 단어의 끝을 알려준다

    def search(self, word):        #주어지는 단어가 있는지 찾는 search함수
        cur = self.head            #cur을 맨위 head로 지정
        for ch in word:            #word의 한 문자가 딕셔너리에 없다면 False반환
            if ch not in cur:
                return False
            cur = cur[ch]          #cur의 위치를 바꿔주며 내려감

        if '*' in cur:             #마지막 내려간자리에 '*'가 있다면 True반환
            return True
        else:
            return False

dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))
print(dictionary.head)
