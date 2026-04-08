import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        # Train the GPT model and return the final loss (rounded to 4 decimals).
        #
        # Steps:
        # 1. Create an AdamW optimizer with the given learning rate
        # 2. For each epoch:
        #    a. Use torch.manual_seed(epoch) for reproducibility
        #    b. Sample random start indices with torch.randint
        #    c. Build X (input) and Y (target) batches, each (batch_size, context_length)
        #       Y is X shifted right by 1
        #    d. Forward pass: logits = model(X), shape (batch_size, context_length, vocab_size)
        #    e. Reshape for cross_entropy: logits to (B*T, C), targets to (B*T)
        #    f. Compute loss = F.cross_entropy(logits_flat, targets_flat)
        #    g. optimizer.zero_grad(), loss.backward(), optimizer.step()
        # 3. Return the final loss value rounded to 4 decimals
        # pass

        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

        for epoch in range(epochs):
            optimizer.zero_grad()
            torch.manual_seed(epoch)
            
            X = torch.zeros((batch_size, context_length), dtype=data.dtype)
            Y = torch.zeros((batch_size, context_length), dtype=data.dtype)
            for i in range(batch_size):
                start = torch.randint(0, len(data)-context_length, (1,)).item()
                x = data[start: start + context_length]
                y = data[start+1: start+1 + context_length]
                X[i] = x
                Y[i] = y
            
            # forward pass
            logits = model(X) 

            B, T, C = logits.shape

            # Reshape for cross_entropy: logits to (B*T, C), targets to (B*T)
            logits_flat = logits.reshape(B*T, C)
            Y_flat = Y.reshape(B*T)

            loss = F.cross_entropy(logits_flat, Y_flat)

            loss.backward()
            optimizer.step()
        
        return round(loss.item(), 4)
            



            
