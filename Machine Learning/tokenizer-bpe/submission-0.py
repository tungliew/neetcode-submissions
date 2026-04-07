from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        # pass

        tokens = list(corpus)
        merges = []

        for num in range(num_merges):
            record = {}

            # iterate the pairs
            for i in range(len(tokens)-1):
                pair = (tokens[i], tokens[i+1])
                record[pair] = record.get(pair, 0) + 1
            
            if not record:
                break

            # find the top pair
            top_pair = min([p for p in record if record[p]==max(record.values())])

            # add top pair to merges
            merges.append([top_pair[0], top_pair[1]])

            # merge
            new_tokens = []
            i = 0
            while i<len(tokens):
                if i<len(tokens)-1 and tokens[i]==top_pair[0] and tokens[i+1]==top_pair[1]:
                    new_tokens.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            
            tokens = new_tokens

        return merges
