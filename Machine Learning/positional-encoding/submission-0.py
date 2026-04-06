import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_positional_encoding(self, seq_len: int, d_model: int) -> NDArray[np.float64]:
        # PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
        # PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
        #
        # Hint: Use np.arange() to create position and dimension index vectors,
        # then compute all values at once with broadcasting (no loops needed).
        # Assign sine to even columns (PE[:, 0::2]) and cosine to odd columns (PE[:, 1::2]).
        # Round to 5 decimal places.
        # pass

        # (seq_len, 1)
        pos = np.arange(seq_len)[:, np.newaxis]
        # (1, d_model)
        i = np.arange(d_model)[np.newaxis, :]

        # (seq_len, d_model)
        angle_rate = 1 / (10000 ** (2 * (i // 2) / d_model))
        angle = pos * angle_rate

        pe = np.zeros((seq_len, d_model))
        pe[:, 0::2] = np.sin(angle[:, 0::2])
        pe[:, 1::2] = np.cos(angle[:, 1::2])

        return np.round(pe, 5)