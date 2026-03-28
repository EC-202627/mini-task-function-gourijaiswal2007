def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate

    capped = False
    if fine > max_fine:
        fine = max_fine
        capped = True

    return fine, capped


# input handling (FIXED)
book_title = input().strip()
days_overdue = int(input().strip())

# optional inputs
try:
    daily_rate = float(input().strip())
except:
    daily_rate = 5.0

try:
    max_fine = float(input().strip())
except:
    max_fine = 150.0


fine, capped = calculate_fine(book_title, days_overdue, daily_rate, max_fine)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

if capped:
    print(f"You have accumulated the maximum fine of INR: {fine}")