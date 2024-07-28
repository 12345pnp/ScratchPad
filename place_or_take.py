#Optimal strategy - N consecutive "places" followed by 100 - N consecutive "takes"
#https://www.quantguide.io/questions/place-or-take

E = lambda x: (1 - 0.5**x)*(100 - x)

optimal_val = (0, 0) #Expected value, Optimal takes
for places in range(1, 101):
    takes = 100 - places
    Eval = E(takes)
    if Eval > optimal_val[0]:
        optimal_val = (Eval, takes)


print(f"The optimal strategy is {100 - optimal_val[1]} places \
followed by {optimal_val[1]} takes, \
with expected value {optimal_val[0]}")
