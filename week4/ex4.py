import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def dot_product_attention(decoder_state, encoder_states):
    """
    decoder_state: numpy array of shape (hidden_size,) -> s_t [cite: 2703]
    encoder_states: list or array of shape (N, hidden_size) -> h_1 ... h_N [cite: 2702]
    """
    
    # 1. TODO: Calculate Attention Scores (dot product) [cite: 2539, 2705]
    # e^t = [s_t^T h_1, ..., s_t^T h_N]
    scores = []
    
    # 2. TODO: Convert scores to a probability distribution using softmax [cite: 2589, 2710]
    # alpha^t = softmax(e^t)
    attention_distribution = []
    
    # 3. TODO: Calculate the weighted sum of encoder states [cite: 2596, 2712]
    # a_t = sum(alpha_i * h_i)
    attention_output = np.zeros_like(decoder_state)
    
    return attention_distribution, attention_output

# --- Testing ---
dec_state = np.array([0.5, 0.2, -0.1])
enc_states = np.array([
    [0.4, 0.2, 0.0],  # state for "il" [cite: 2540]
    [-0.1, 0.9, 0.2], # state for "a"
    [0.6, 0.1, -0.3]  # state for "m'"
])

distribution, context_vector = dot_product_attention(dec_state, enc_states)
print("Attention Distribution:", distribution)
print("Attention Context Vector:", context_vector)
