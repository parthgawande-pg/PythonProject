
nums = tuple(map(int, input("Enter integers separated by space: ").split()))


print("Total items:", len(nums))


print("Last item:", nums[-1])


print("Reversed tuple:", nums[::-1])


if 5 in nums:
    print("Yes")
else:
    print("No")


new_tuple = nums[1:-1]
sorted_tuple = tuple(sorted(new_tuple))

print("After removing first & last and sorting:", sorted_tuple)