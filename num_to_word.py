
digit_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teen_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def number_to_words(num):
    if num == 0:
        return ""
    
 
    if num >= 1000:
        return digit_words[num // 1000] + " thousand " + number_to_words(num % 1000)
    

    if num >= 100:
        return digit_words[num // 100] + " hundred " + number_to_words(num % 100)
    

    if num >= 20:
        return tens_words[num // 10] + " " + digit_words[num % 10]
    

    if num >= 10:
        return teen_words[num % 10]
    

    # return digit_words[num]


num = int(input("Enter a four-digit number: "))

if num == 0:
    print("zero")
else:
    print(number_to_words(num))
