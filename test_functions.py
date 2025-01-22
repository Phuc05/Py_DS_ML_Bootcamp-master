import pandas as pd
import numpy as np
import cufflinks as cf

cf.go_offline()

# Create a sample DataFrame
np.random.seed(42)
df = pd.DataFrame({
    'A': np.random.rand(100) * 100,
    'B': np.random.rand(100) * 50
})

# Use a valid color format
color = 'rgb(255,153,51)'  # Orange color

# Plot the scatter plot
df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10, color=color)
