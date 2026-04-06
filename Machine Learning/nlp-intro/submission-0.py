import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        # pass

        words = set()
        # ["Dogecoin to the moon"]
        for sentence in positive+negative:
            words.update(sentence.split())
        
        words = sorted(words)
        word_dict = {word: i + 1 for i, word in enumerate(words)}

        # encoding sentences
        tensors = []

        for pos_str in positive:
            ids = [word_dict[word] for word in pos_str.split()]
            tensors.append(torch.tensor(ids))
        
        for neg_str in negative:
            ids = [word_dict[word] for word in neg_str.split()]
            tensors.append(torch.tensor(ids))
        
        padded_tensors = nn.utils.rnn.pad_sequence(tensors, batch_first=True, padding_value=0)

        return padded_tensors