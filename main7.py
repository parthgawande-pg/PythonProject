prices = tuple(map(int, input("Enter item prices separated by space: ").split()))

print("Total items sold:", len(prices))

print("Cheapest item price:", min(prices))

max_price = max(prices)
print("Costliest item price:", max_price)

print("Prices in ascending order:", tuple(sorted(prices)))

count_max = prices.count(max_price)
print("Number of costliest items sold:", count_max)