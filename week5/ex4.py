class PreLNTransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        
        # Multi-Head Attention
        self.mha = nn.MultiheadAttention(embed_dim=d_model, num_heads=num_heads, batch_first=True)
        
        # Feed-Forward Network (Non-linearities)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model)
        )
        
        # Layer Normalization modules
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        """
        Args:
            x: Input tensor of shape (batch_size, seq_len, d_model)
            mask: Optional boolean tensor for causal masking
        """
        # --- Pre-LN Attention ---
        # 1. TODO: Apply LayerNorm1 to x BEFORE passing to attention
        norm_x = self.norm1(x)
        
        # 2. TODO: Pass norm_x into MultiheadAttention. 
        # Note: PyTorch MHA takes (query, key, value). Here, all three are norm_x.
        attn_output, _ = self.mha(norm_x, norm_x, norm_x, attn_mask=mask)
        
        # 3. TODO: Apply residual connection (Add the ORIGINAL x to the attention output)
        x = x + self.dropout(attn_output)
        
        # --- Pre-LN Feed-Forward ---
        # 4. TODO: Apply LayerNorm2 to x, pass it through FFN, and apply the second residual
        norm_x2 = self.norm2(x)
        ffn_output = self.ffn(norm_x2)
        x = x + self.dropout(ffn_output)
        
        return x

# --- TEST YOUR CODE ---
d_model = 64
num_heads = 8
d_ff = 256
batch_size = 2
seq_len = 10

block = PreLNTransformerBlock(d_model, num_heads, d_ff)
dummy_input = torch.randn(batch_size, seq_len, d_model)
output = block(dummy_input)

print(f"Transformer Block Output Shape: {output.shape}")
