import streamlit as st
import numpy as np
from viz import create_line_plot
import matplotlib.pyplot as plt

st.title('📊 Interactive Plot Demo')

# Create sidebar controls
st.sidebar.header('Plot Controls')
wave_type = st.sidebar.selectbox(
    'Select Wave Type',
    ['Sine', 'Cosine', 'Linear']
)

color = st.sidebar.color_picker('Choose line color', '#0000FF')

# Generate data based on selection
x = np.linspace(0, 10, 100)
if wave_type == 'Sine':
    y = np.sin(x)
    title = 'Sine Wave'
elif wave_type == 'Cosine':
    y = np.cos(x)
    title = 'Cosine Wave'
else:
    y = x
    title = 'Linear Function'

# Create the plot
fig = plt.figure(figsize=(10, 6))
plt.plot(x, y, color=color)
plt.title(title)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot in Streamlit
st.pyplot(fig)

# Add some explanation
st.write("""
This interactive plot allows you to:
- Choose between different wave types
- Customize the line color
- View the resulting plot in real-time
""")


# add your code here