import plotly.express as px

from die import Die

# Create a six-sided die
die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

poss_results = range(1, die.num_sides + 1)
frequencies = [results.count(x) for x in poss_results]

print(frequencies)

title = "Results of Rolling One D6 1,000 Times"
lables = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=lables)
fig.show(renderer="browser")
