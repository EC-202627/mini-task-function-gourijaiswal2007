def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate

    if fine > max_fine:
        fine = max_fine
        return fine, True
    else:
        return fine, False


# input lena (flexible input)
data = input().split()

# last values numeric hote hain, baaki title
nums = []
title_words = []

for x in data:
    try:
        nums.append(float(x))
    except:
        title_words.append(x)

book_title = " ".join(title_words)

days_overdue = int(nums[0])

# optional parameters
if len(nums) == 1:
    fine, capped = calculate_fine(book_title, days_overdue)

elif len(nums) == 2:
    fine, capped = calculate_fine(book_title, days_overdue, nums[1])

else:
    fine, capped = calculate_fine(book_title, days_overdue, nums[1], nums[2])


# output
print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

if capped:
    print(f"You have accumulated the maximum fine of INR: {fine}")
