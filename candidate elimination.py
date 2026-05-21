import pandas as pd
import numpy as np

data = pd.read_csv("2.csv")

X = np.array(data.iloc[:, :-1])
y = np.array(data.iloc[:, -1])

S = X[0].copy()

G = [["?" for i in range(len(S))]
     for i in range(len(S))]

for i in range(len(X)):

    if y[i] == "yes":

        for j in range(len(S)):

            if X[i][j] != S[j]:
                S[j] = "?"
                G[j][j] = "?"

    elif y[i] == "no":

        for j in range(len(S)):

            if X[i][j] != S[j]:
                G[j][j] = S[j]
            else:
                G[j][j] = "?"

G = [x for x in G if x != ['?','?','?','?','?','?']]

print("Specific Hypothesis:")
print(S)

print("General Hypothesis:")
print(G)
