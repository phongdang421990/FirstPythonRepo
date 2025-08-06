def get_number(prompt, default=1):
    user_input = input(prompt)
    return int(user_input) if user_input.strip() else default

# Gọi hàm nhập từ người dùng
a = get_number("Nhập số a (mặc định = 1): ")
b = get_number("Nhập số b (mặc định = 1): ")

# Tính tổng và hiệu
calc = lambda a, b: (a + b, a - b)
result = calc(a, b)

# In kết quả ra
print(f"Tổng: {result[0]}, Hiệu: {result[1]}") 