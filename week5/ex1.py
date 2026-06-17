import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def scaled_dot_product_attention(q, k, v, mask=None):
    """
    Computes scaled dot-product attention.
    Args:
        q: Queries tensor of shape (batch_size, num_heads, seq_len, d_k)
        k: Keys tensor of shape (batch_size, num_heads, seq_len, d_k)
        v: Values tensor of shape (batch_size, num_heads, seq_len, d_v)
        mask: Optional tensor to mask future tokens (causal masking)
    Returns:
        output: The attention output
        attn_weights: The attention probabilities
    """
    d_k = q.size(-1)
    
    # 1. TODO: Compute the dot product between queries and keys. 
    # Hint: You will need to transpose the last two dimensions of k.
    scores = torch.matmul(q, k.transpose(-2, -1))
    
    # 2. TODO: Scale the scores by the square root of d_k to prevent vanishing gradients
    scores = scores / math.sqrt(d_k)
    
    # 3. Apply the causal mask if provided (sets masked positions to -infinity)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
        
    # 4. TODO: Apply the softmax function to the scores along the last dimension to get probabilities
    attn_weights = F.softmax(scores, dim=-1)
    
    # 5. TODO: Multiply the attention weights by the values vector
    output = torch.matmul(attn_weights, v)
    
    return output, attn_weights

# --- TEST YOUR CODE ---
q = torch.randn(1, 1, 4, 64) # (batch=1, heads=1, seq_len=4, d_k=64)
k = torch.randn(1, 1, 4, 64)
v = torch.randn(1, 1, 4, 64)

output, weights = scaled_dot_product_attention(q, k, v)
print(f"Output shape (should be [1, 1, 4, 64]): {output.shape}")
print(f"Weights shape (should be [1, 1, 4, 4]): {weights.shape}")
