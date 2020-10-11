import pandas as pd
import matplotlib.pyplot as plt
data = (12,
13,
23,
31,
45,
47,
48,
51,
54,
59,
60,
60,
70,
87,
93,
100,
101,
115,
118,
123,
143,
)

commutes = pd.Series(data)

commutes.plot.hist(grid=True, bins=10, rwidth=0.9,
                   color='#607c8e')
plt.title('Time between reinfections')
plt.ylabel('Counts')
plt.xlabel('Reinfection interval')
