import numpy as np

# Let's assume we have a sequence of 3 word embeddings
seq_len = 3
embed_size = 4
hidden_size = 2

sequence = [np.random.randn(embed_size) for _ in range(seq_len)]

# Dummy weights for Forward and Backward RNNs [cite: 2247]
W_h_fw = np.random.randn(hidden_size, hidden_size)
W_e_fw = np.random.randn(hidden_size, embed_size)
W_h_bw = np.random.randn(hidden_size, hidden_size)
W_e_bw = np.random.randn(hidden_size, embed_size)

# 1. TODO: Process the sequence forward
h_fw = np.zeros(hidden_size)
forward_states = []
for x in sequence:
    # Use the rnn_step function from Exercise 2
    pass 

# 2. TODO: Process the sequence backward
h_bw = np.zeros(hidden_size)
backward_states = []
for x in reversed(sequence):
    # Process from the end of the sequence to the beginning
    pass
# Remember to reverse backward_states so it aligns with forward_states!

# 3. TODO: Concatenate the states
final_states = []
for i in range(seq_len):
    # Concatenate forward_states[i] and backward_states[i]
    pass

print("Final concatenated states shape:", np.array(final_states).shape)
