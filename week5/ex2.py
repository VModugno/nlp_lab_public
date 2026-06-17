def create_causal_mask(seq_len):
    """
    Creates a causal mask for an autoregressive decoder.
    Args:
        seq_len: The length of the sequence
    Returns:
        mask: A tensor of shape (seq_len, seq_len) containing 1s (allow) and 0s (block)
    """
    # TODO: Use PyTorch's torch.tril() to create a lower triangular matrix of ones.
    # This ensures position 'i' can only attend to positions '<= i'.
    mask = torch.tril(torch.ones(seq_len, seq_len))
    
    # Reshape for broadcasting with batch and head dimensions
    return mask.view(1, 1, seq_len, seq_len)

# --- TEST YOUR CODE ---
seq_len = 4
mask = create_causal_mask(seq_len)
print("Causal Mask:\n", mask[0, 0])
# Expected Output:
# tensor([[1., 0., 0., 0.],
#         [1., 1., 0., 0.],
#         [1., 1., 1., 0.],
#         [1., 1., 1., 1.]])
