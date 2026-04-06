import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        # pass
        max_val = np.max(z)
        exp_vals = np.exp(z - max_val)
        probs = exp_vals / np.sum(exp_vals)

        return np.round(probs, 4)
