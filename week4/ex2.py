import numpy as np

def rnn_step(h_prev, x_t, W_h, W_e, b):
    """
    Performs one timestep update of a Vanilla RNN.
    
    Parameters:
    h_prev : numpy array, the previous hidden state
    x_t    : numpy array, the input embedding at current timestep
    W_h    : numpy array, the hidden state weight matrix
    W_e    : numpy array, the input embedding weight matrix
    b      : numpy array, the bias vector
    
    Returns:
    h_curr : the new hidden state
    """
    # 1. TODO: Implement the RNN update equation
    # Hint: use np.dot() for matrix multiplication and np.tanh() for activation
    
    h_curr = None # Replace with your equation
    return h_curr

# --- Testing ---
hidden_size = 4
embed_size = 5

# Initialize random weights and inputs
W_h = np.random.randn(hidden_size, hidden_size)
W_e = np.random.randn(hidden_size, embed_size)
b = np.zeros(hidden_size)

h_0 = np.zeros(hidden_size) # Initial memory state [cite: 1685]
x_1 = np.random.randn(embed_size) # Word embedding for step 1

h_1 = rnn_step(h_0, x_1, W_h, W_e, b)
print("Updated Hidden State h_1:", h_1)
