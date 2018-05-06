twenty = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}

tens = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}

def base(num):
    if num < 20:
        return twenty[num]

    if num < 100:
        return (tens[num / 10] + ' ' + base(num % 10)).strip()

    if num < 1000:
        return (twenty[num / 100] + ' Hundred ' + base(num % 100)).strip()

    if num < 1000000:
        return (base(num / 1000) + ' Thousand ' + base(num % 1000)).strip()

    if num < 1000000000:
        return (base(num / 1000000) + ' Million ' + base(num % 1000000)).strip()

    return (base(num / 1000000000) + ' Billion ' + base(num % 1000000000)).strip()

def numberToWords(num):
    res = base(num)
    return res
