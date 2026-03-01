import numpy as np
identity_matrix = np.eye(4)

print("4x4 Identity Matrix:")
print(identity_matrix)



import numpy as np
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

addition = A + B
print("\nAddition of A and B:")
print(addition)

multiplication = np.dot(A, B)
print("\nMultiplication of A and B:")
print(multiplication)