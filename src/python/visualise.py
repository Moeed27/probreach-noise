import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys

# the last element is the full path to the file
data = pd.read_json(sys.argv[-1])

# Creating subplots for all variables specified
if len(sys.argv) > 2:
    num_vars = len(sys.argv) - 2
    fig, axes = plt.subplots(nrows=num_vars, ncols=1, sharex=True)
    if num_vars == 1:
        axes = [axes]
else:
    fig, ax = plt.subplots()
    axes = [ax]

# Create custom legend handles
custom_lines = [
    Line2D([0], [0], color='green', lw=2, label='Goal Reached'),
    Line2D([0], [0], color='red', lw=2, alpha=0.1, label='Goal Not Reached')
]

# iterating through all trajectories
for i in range(0,len(data['trajectories'])):
	df = pd.DataFrame(data['trajectories'][i]['values'])

	color = 'red'
	opacity = 0.1
	goal_reached = data['trajectories'][i]['reached']
	
	if goal_reached:
		color = 'green'
		opacity = 1

	# checking if any variables for plotting are specified
	if(len(sys.argv) <= 2):
		df.plot(x='.global_time', ax=axes[0], title='Trajectory')
	else:
		# iterating through the specified variables
		for j in range(1, len(sys.argv)-1):
			if(sys.argv[j] == '--all'):
				df.plot(x='.global_time', ax=axes[j-1])
			else:
				df.plot(x='.global_time', y=sys.argv[j], ax=axes[j-1], label=f'Trajectory {i+1}', color=color, alpha=opacity, legend=False)
				axes[j-1].set_ylabel(sys.argv[j])

fig.legend(handles=custom_lines, loc='upper right', bbox_to_anchor=(1, 1))
plt.suptitle(f'Trajectories')
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.savefig('output_plot.png')