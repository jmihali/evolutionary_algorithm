This experiment aims a deeper testing of crossover. For the testing, I used the following multivariate test function, 
called Alpine 2 Function, with n = 5 dimensions:

- <img src="https://latex.codecogs.com/gif.latex? f(\mathbf x)=f(x_1, ..., x_n) = \prod_{i=1}^{n}\sqrt{x_i}sin(x_i) " />

The global minimum is located at x∗= (7.917, ... , 7.917), f(x*) = 2.808^n.
Throughout the experiment, the following options are kept fixed:
```python
DIMENSIONS = 5
population size = 200
generations = 20
toolbox.register('attr_float', random.uniform, 0, 10)
toolbox.register('select', tools.selTournament, tournsize=3)
MUTPB = 0
```

##1. Trying different kinds of crossover
For each of the following, the experiment was repeated 100 times, each time with a different initialization.
In each subsection, we show the experiment that got the best result. 
###A) Single Point Crossover 
Experiments with a score better than -120: 30/100
Experiments with a score better than -150: 15/100
Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [8.11240237 7.93968618 7.84714226 7.8010144  7.94624159]
Best fitness: -169.5334137823707

![alt text](Figure_1.png)

###B) Two Point Crossover 
Experiments with a score better than -120: 59/100
Experiments with a score better than -150: 29/100
Experiments with a score better than -170: 1/100

Best experimental result:

Best individual:  [8.04540554 7.80556469 8.04510261 7.86414926 7.95450242]
Best fitness: -170.27786525997797

![alt text](Figure_2.png)

###C) Uniform Crossover with indpb=0.3 
Experiments with a score better than -120: 80/100
Experiments with a score better than -150: 60/100
Experiments with a score better than -170: 5/100

Best experimental result:

Best individual:  [7.96937432 7.96477533 7.97544575 7.97059479 7.81864992]
Best fitness: -172.7732086493284

![alt text](Figure_3.png)
