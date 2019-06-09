import kadai1_4

print(kadai1_4.k2(4,0.01))
print(kadai1_4.k3(4,0.01))

# further test cases
# さらなるテストケース
print("\nusing 1_2")
print(kadai1_4.k2(0,0.01))
print(kadai1_4.k2(1,0.01))
print(kadai1_4.k2(0.01,0.01))
print(kadai1_4.k2(0.25,0.01))
print(kadai1_4.k2(0.99,0.01))
print(kadai1_4.k2(1.01,0.01))
print(kadai1_4.k2(1000,0.01))
print(kadai1_4.k2(9999999999,0.01))
print(kadai1_4.k2(125678765432345678987654,0.01))

print("\nusing 1_3")
print(kadai1_4.k3(0,0.01))
print(kadai1_4.k3(1,0.01))
print(kadai1_4.k3(0.01,0.01))
print(kadai1_4.k3(0.25,0.01))
print(kadai1_4.k3(0.99,0.01))
print(kadai1_4.k3(1.01,0.01))
print(kadai1_4.k3(1000,0.01))
print(kadai1_4.k3(9999999999,0.01))
print(kadai1_4.k3(125678765432345678987654,0.01))
