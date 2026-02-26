def spiral_diagonals_sum_loop(n: int) -> int:
    total = 1
    for k in range(1, (n - 1) // 2 + 1):
        total += 16*k*k + 4*k + 4
    return total

print(spiral_diagonals_sum_loop(1001))  
