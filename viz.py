import matplotlib.pyplot as plt
import numpy as np

def create_line_plot(x_data, y_data, title="Line Plot", x_label="X Axis", y_label="Y Axis", color='blue'):
    """
    Create a line plot using matplotlib.
    
    Args:
        x_data: Data for x-axis
        y_data: Data for y-axis
        title: Plot title (default: "Line Plot")
        x_label: Label for x-axis (default: "X Axis")
        y_label: Label for y-axis (default: "Y Axis")
        color: Line color (default: 'blue')
    Returns:
        matplotlib.figure.Figure: The created plot figure
    """
    # Create the figure and axis
    fig = plt.figure(figsize=(10, 6))
    
    # Create the line plot
    plt.plot(x_data, y_data, color=color)
    
    # Add title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    return fig
