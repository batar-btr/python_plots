import plotly.express as px

from die import Die

# Create 2 six-sided dice
die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(x) for x in poss_results]

print(frequencies)

title = "Results of Rolling Two D6 1,000 Times"
lables = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=lables)

fig.update_layout(xaxis_dtick=1)
fig.write_html('plot.html')
