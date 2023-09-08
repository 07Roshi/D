# def knapsack_max_profit(weights,costs,capacity):
#   num_items=len(weights)
#   table=[[0]*(capacity+1) for _ in range(num_items+1)]
#   for i in range(1,num_items+1):
#     for j in range(1,capacity+1):
#       if weights[i-1]<=j:
#         table[i][j] = max(costs[i-1]+table[i-1][j-weights[i-1]],table[i-1][j])
        
#       else:
#         table[i][j]=table[i-1][j]
#   selected_items=[]
#   total_weight=capacity
#   for i in range(num_items,0,-1):
#     if table[i][total_weight]!=table[i-1][total_weight]:
#       selected_items.append(i-1)
#       total_weight==weights[i-1]
#   return table[num_items][capacity],selected_items
# # weights=[2,3,4,5]
# # costs=[10,20,30,40]
# # capacity=10
# weights = input("Enter the weights of the items: ").split()
# weights = [int(w) for w in weights]
# costs = input("Enter the costs of the items: ").split()
# costs = [int(c) for c in costs]
# capacity = int(input("Enter the capacity of the knapsack: "))
# max_profit,selected_items=knapsack_max_profit(weights,costs,capacity)
# print("maximun profit: ",max_profit)
# print("selected coffee beans (index): ",selected_items)
# print("selected coffee beans (weights): ",[weights[i]for i in selected_items])
# print("selected coffee beans (costs): ",[costs[i]for i in selected_items])


def knapsack_max_profit(weights, costs, capacity):
    num_items = len(weights)
    table = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    
    for i in range(1, num_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(costs[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    
    selected_items = []
    total_weight = capacity
    i = num_items
    
    while i > 0 and total_weight > 0:
        if table[i][total_weight] != table[i - 1][total_weight]:
            selected_items.append(i - 1)
            total_weight -= weights[i - 1]
        i -= 1
    
    return table[num_items][capacity], selected_items


weights = [int(w) for w in input("Enter the weights of the items: ").split()]
costs = [int(c) for c in input("Enter the costs of the items: ").split()]
capacity = int(input("Enter the capacity of the knapsack: "))

max_profit, selected_items = knapsack_max_profit(weights, costs, capacity)

print("Maximum profit:", max_profit)
print("Selected items (index, weight, cost):")
for i in selected_items:
    print(i, weights[i], costs[i])
