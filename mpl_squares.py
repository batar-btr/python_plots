import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import random

# Define colors
BG_COLOR = '#222d3b'
DOT_COLOR = '#a975fd'  # or use 'lime' or (0, 1, 0)
FONT_COLOR = "#cacaca"

plt.rcParams['figure.facecolor'] = BG_COLOR
squares = [x**2 for x in range(1, 14)]

prices = [random.randint(500, 2000) for x in range(20)]
prices2 = [random.randint(500, 2000) for x in range(20)]


nums = range(100)
squares2 = [x**2 for x in nums]

fig, ax = plt.subplots()

for spine in ax.spines.values():
    spine.set_visible(False)

# ax.plot(sorted(prices), marker='o', label='line 1')
# ax.plot(prices2, marker='o', label='line 2')
for _ in range(6):
    y = [random.randint(1, 100) for _ in range(random.randint(20, 40))]
    ax.plot(sorted(y), marker='o', label='line 1')
# random.shuffle(squares2)

# Set scatter plot with proper colors
# ax.scatter(nums, squares2,
#            cmap=plt.cm.cool,
#            c=squares2,  # Color of dots
#            s=10,         # Size of dots
#            alpha=0.6)    # Optional: transparency

# Style the plot
ax.set_facecolor(BG_COLOR)
ax.set_title("Square Numbers", fontsize=24, color=FONT_COLOR)  # White text
ax.set_xlabel("Value", color=FONT_COLOR)
ax.set_ylabel("Square of Value", color=FONT_COLOR)
ax.tick_params(colors=FONT_COLOR)  # White tick labels
ax.grid(True, color='gray', alpha=0.1)  # Subtle grid

# Force integer ticks on x-axis
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# plt.legend()
plt.show()
