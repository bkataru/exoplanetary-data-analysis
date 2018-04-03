
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

planets = pd.read_csv("planets.csv", sep=',')
sns.set(style="ticks")

# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")

# Load the example planets dataset

# replace pl_pnum and st_mass with other column names
sns.boxplot(x="st_mass", y="pl_discmethod", data=planets)

# Add in points to show each observation
sns.swarmplot(x="st_mass", y="pl_discmethod", data=planets,
              size=2, color=".3", linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)