max_retries = 3
attempt = 0
while attempt < max_retries:
    print(f"Attempt {attempt + 1}")
    attempt += 1
else:
    print("All attempts done!")