class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        
        # Create a matrix of shape (max_len, d_model) full of zeros
        pe = torch.zeros(max_len, d_model)
        
        # Create a tensor of shape (max_len, 1) with positions (0, 1, 2... max_len)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        
        # 1. TODO: Compute the scaling factor: exp(-2i * log(10000) / d_model)
        # Note: We compute it in log space for numerical stability.
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        
        # 2. TODO: Apply sine to even indices (0, 2, 4...)
        pe[:, 0::2] = torch.sin(position * div_term)
        
        # 3. TODO: Apply cosine to odd indices (1, 3, 5...)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        pe = pe.unsqueeze(0) # Shape: (1, max_len, d_model)
        self.register_buffer('pe', pe)

    def forward(self, x):
        # 4. TODO: Add the positional encoding to the input embeddings 'x'
        # x shape: (batch_size, seq_len, d_model)
        seq_len = x.size(1)
        x = x + self.pe[:, :seq_len, :]
        return x

# --- TEST YOUR CODE ---
d_model = 16
seq_len = 10
pos_encoder = PositionalEncoding(d_model)
dummy_embeddings = torch.zeros(1, seq_len, d_model) # Zero embeddings to just see the PE
encoded = pos_encoder(dummy_embeddings)
print(f"Encoded shape: {encoded.shape}")
