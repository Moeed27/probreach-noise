import pandas as pd
import matplotlib.pyplot as plt
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

# itterating through all trajectories
for i in range(0,len(data['trajectories'])):
	df = pd.DataFrame(data['trajectories'][i])
	# checking if any variables for plotting are specified
	if(len(sys.argv) <= 2):
		df.plot(x='.global_time', ax=axes[0], title='Trajectory')
	else:
		# iterating through the specified variables
		for j in range(1, len(sys.argv)-1):
			if(sys.argv[j] == '--all'):
				df.plot(x='.global_time', ax=axes[j-1])
			else:
				df.plot(x='.global_time', y=sys.argv[j], ax=axes[j-1], label=f'Trajectory {i+1}', color='blue', legend=False)

plt.suptitle(f'Trajectories')
plt.tight_layout()
plt.savefig('output_plot.png')