class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # *가 있을 경우, 그 단어가 자료구조에 저장되어 있음을 의미
        # *가 없을 경우, 그 단어는 자료구조에 저장되어 있지 않음, 단지 더 긴 단어의 부분으로만 존재함
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
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
print({})
#{'h': {'i': {'*': True}, 'e': {'l': {'l': {'o': {'*': True}}}}}}