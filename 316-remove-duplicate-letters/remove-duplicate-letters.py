class Solution(object):
    def removeDuplicateLetters(self, s):
        last_pos = {char: i for i, char in enumerate(s)}
        string_builder = []
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while string_builder and char < string_builder[-1] and i < last_pos[string_builder[-1]]:
                    seen.discard(string_builder.pop())

                seen.add(char)
                string_builder.append(char)

        return "".join(string_builder)