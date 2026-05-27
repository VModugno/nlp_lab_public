import numpy as np
import math

# Simulated probabilities for the Target "dog" and Context "eat"
p_target_dog = 0.05       # P(t)
p_context_eat = 0.02      # P(c)
p_dog_and_eat = 0.004     # P(t,c) (They co-occur 0.4% of the time)

def calculate_ppmi(p_tc, p_t, p_c):
    # TODO: Implement the PPMI formula: max(0, log2( P(t,c) / (P(t)*P(c)) ))
    if p_tc == 0 or p_t == 0 or p_c == 0:
        return 0.0
    
    # Calculate the ratio
    ratio = p_tc / (p_t * p_c)
    
    # Calculate log base 2
    log_val = math.log2(ratio)
    
    # Apply max(0, x) to ensure it is POSITIVE PMI
    return max(0, log_val)

ppmi_score = calculate_ppmi(p_dog_and_eat, p_target_dog, p_context_eat)
print(f"The PPMI score for 'dog' and 'eat' is: {ppmi_score:.2f}")

# Question for the student:
# If p_dog_and_eat was exactly equal to (p_target_dog * p_context_eat), what would the PPMI score be? Why?
