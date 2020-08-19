This experiment aims to test mutation. As in the previous experiment, for the testing I used the following multivariate test function, 
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
CXPB = 0.0
```

## Trying Gaussian Mutation
indpb=0.2

### Sigma = 0.0001, MUTPB = 0.05

Experiments with a score better than -120: 1/100

Experiments with a score better than -150: 0/100

Experiments with a score better than -170: 0/100


Best experimental result:

Best individual:  [7.68760211 7.45991805 8.27374169 7.52347948 7.83720263]
Best fitness: -131.5430826039821


### Sigma = 0.1, MUTPB = 0.05

Experiments with a score better than -120: 6/100

Experiments with a score better than -150: 2/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [7.65782858 7.6716754  8.15884844 7.82864398 7.82815005]

Best fitness: -157.59097116496636

### Sigma = 0.4, MUTPB = 0.05

Experiments with a score better than -120: 12/100

Experiments with a score better than -150: 9/100

Experiments with a score better than -170: 3/100

Best experimental result:

Best individual:  [7.80922011 7.84660974 7.90476101 8.07414791 7.89841957]

Best fitness: -170.946248676026


### Sigma = 0.5, MUTPB = 0.05

Experiments with a score better than -120: 14/100

Experiments with a score better than -150: 11/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [7.83990288 7.87566843 7.89244799 7.75836705 7.75701566]

Best fitness: -169.48751554032643

### Sigma = 1, MUTPB = 0.05

Experiments with a score better than -120: 13/100

Experiments with a score better than -150: 8/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [8.06790972 7.80450368 7.90167424 8.03431461 7.83721169]

Best fitness: -169.73295598610318

### Sigma = 2, MUTPB = 0.05

Experiments with a score better than -120: 11/100

Experiments with a score better than -150: 3/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [7.78328012 7.97182511 7.92662876 7.79391156 8.24560824]

Best fitness: -162.0546786122609

### Sigma = 5, MUTPB = 0.05

Experiments with a score better than -120: 7/100

Experiments with a score better than -150: 3/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [7.91159515 7.99398148 8.11939953 7.58310227 7.89507131]

Best fitness: -161.0299502863081

### Sigma = 10000, MUTPB = 0.05

Experiments with a score better than -120: 1/100

Experiments with a score better than -150: 0/100

Experiments with a score better than -170: 0/100

Best experimental result:

Best individual:  [7.68760211 7.45985791 8.27398174 7.52300274 7.83721169]

Best fitness: -131.5014768122428


### Sigma = 0.4, MUTPB = 0.01

Experiments with a score better than -120: 6/100

Experiments with a score better than -150: 3/100

Experiments with a score better than -170: 0/100


Best experimental result:

Best individual:  [8.02045407 8.13951074 7.51816622 7.84198769 7.79969418]
Best fitness: -154.5528981137419

### Sigma = 0.4, MUTPB = 0.1

Experiments with a score better than -120: 15/100

Experiments with a score better than -150: 13/100

Experiments with a score better than -170: 6/100


Best experimental result:

Best individual:  [7.9502395  7.87428387 8.00565543 7.97053879 7.88091306]

Best fitness: -173.29760258149463

### Sigma = 0.4, MUTPB = 0.2

Experiments with a score better than -120: 18/100

Experiments with a score better than -150: 18/100

Experiments with a score better than -170: 12/100

Best experimental result:

Best individual:  [7.8805191  7.91593064 7.87952614 7.92052157 7.85330587]

Best fitness: -174.01666157547197

### Sigma = 0.4, MUTPB = 0.4

Experiments with a score better than -120: 20/100

Experiments with a score better than -150: 20/100

Experiments with a score better than -170: 16/100


Best experimental result:

Best individual:  [7.93007125 7.94019998 7.95430737 7.85667116 7.89118557]
Best fitness: -174.0522890506143

### Sigma = 0.4, MUTPB = 0.5

Experiments with a score better than -120: 20/100

Experiments with a score better than -150: 20/100

Experiments with a score better than -170: 18/100

Best experimental result:

Best individual:  [7.92075154 7.91347936 7.87486861 7.95375576 7.90852861]

Best fitness: -174.33242617804953

### Sigma = 0.4, MUTPB = 0.9

Experiments with a score better than -120: 23/100

Experiments with a score better than -150: 23/100

Experiments with a score better than -170: 22/100

Best experimental result:

Best individual:  [7.91451943 7.92454113 7.92308392 7.9315934  7.91056388]

Best fitness: -174.586028578492

## Testing Polynomial Mutation
Parameters to fix:
* Eta - the higher it is, the more the mutant will resemble its parent (analogous to the inverse of sigma)
* Low and Up - the boundaries of the search space, I fixed them to 0 and 10
MUTPB = 0.4

### Eta = -1000 (High variance)

Experiments with a score better than -120: 1/100

Experiments with a score better than -150: 0/100

Experiments with a score better than -170: 0/100


Best experimental result:

Best individual:  [7.68760211 7.45985791 8.27398174 7.52300274 7.83721169]
Best fitness: -131.5014768122428




### Eta = 0.1

Experiments with a score better than -120: 62/100

Experiments with a score better than -150: 41/100

Experiments with a score better than -170: 4/100


Best experimental result:

Best individual:  [7.89044868 7.99813482 7.88680626 7.83123741 7.89558728]
Best fitness: -173.20641128135048


## Eta = 1

Experiments with a score better than -120: 62/100

Experiments with a score better than -150: 43/100

Experiments with a score better than -170: 6/100


Best experimental result:

Best individual:  [7.99454752 7.84980959 7.89127017 7.86640059 7.8365431 ]
Best fitness: -172.83837679343785

### Eta = 10

Experiments with a score better than -120: 22/100

Experiments with a score better than -150: 21/100

Experiments with a score better than -170: 9/100


Best experimental result:

Best individual:  [7.94976322 7.93240922 7.87757012 7.89833298 7.93833122]
Best fitness: -174.29342026853124

### Eta = 100

Experiments with a score better than -120: 16/100

Experiments with a score better than -150: 12/100

Experiments with a score better than -170: 5/100


Best experimental result:

Best individual:  [7.89827942 7.91740447 7.85053078 7.90641729 7.85433147]
Best fitness: -173.84068402798127

### Eta = 1000 (low variance)

Experiments with a score better than -120: 3/100

Experiments with a score better than -150: 0/100

Experiments with a score better than -170: 0/100


Best experimental result:

Best individual:  [7.70482132 7.58629519 8.23699607 7.55126684 7.85378922]

Best fitness: -142.67736357921183

Observation: Similarly to the Gaussian mutation, increasing the variance of the mutation leads to a more effective
optimization, because you introduce more variety to the population.

Having a super high or a super low variance are both bad. In the first case, good solutions are destroyed. In the latter,
there will be no diversity.

## Testing Shuffle Indexes mutation

MUTPB = 0.4

Experiments with a score better than -120: 1/100

Experiments with a score better than -150: 0/100

Experiments with a score better than -170: 0/100


Best experimental result:

Best individual:  [7.52300274 7.45985791 7.83721169 7.68760211 8.27398174]
Best fitness: -131.50147681224283

Performs poorly for this optimization problem. In another kind of problem it should perform well (e.g. 'find the
permutation of M different symbols that has the best fitness')


