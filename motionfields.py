"""Functions to plot precipitation fields."""

import matplotlib.pylab as plt
import matplotlib.colors as colors

import numpy as np

def plot_motion_field_quiver(V, step=10):
    """Function to plot a precipitation field witha a colorbar. 
    
    Parameters 
    ---------- 
    V : array-like 
        Array of shape (2, m,n) containing the input motion field.
    
    units : str
        Units of the input array (px/step, kmh) 
    
    Returns: 
    ----------
    ax : fig axes
        Figure axes. Needed if one wants to add e.g. text inside the plot.
    
    """
    
    idx_valid_rows = np.arange(0, V.shape[1])
    idx_valid_cols = np.arange(0, V.shape[2])
    V[~idx_valid_rows, ~idx_valid_cols] = np.nan
    
    # Plot motion field
    im = plt.quiver(V[0,:,:], -V[1,:,:])
    
    axes = plt.gca()
    
    return(axes)