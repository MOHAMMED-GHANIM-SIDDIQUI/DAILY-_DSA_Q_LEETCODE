from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float("inf")


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        # Build reversed trie
        for idx, word in enumerate(wordsContainer):
            node = root
            wlen = len(word)

            # Update root best match
            if wlen < node.best_len:
                node.best_len = wlen
                node.best_idx = idx

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store shortest word index at each node
                if wlen < node.best_len:
                    node.best_len = wlen
                    node.best_idx = idx

        ans = []

        # Query
        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_idx)

        return ans
