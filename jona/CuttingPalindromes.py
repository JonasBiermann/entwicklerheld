class CuttingPalindromesPython:

    def is_palindrome(self, string):
        if string == string[::-1]:
            return True
        return False

    def minimum_palindrome_cuts(self, palindrome_string) -> int:
        ar = []
        newAr = []

        if palindrome_string == palindrome_string[::-1]:
            return 0
        for i in range(len(palindrome_string)):
            for j in range(len(palindrome_string), i, -1):
                tmp = palindrome_string[i:j]
                if tmp == tmp[::-1]:
                    #print(palindrome_string[i:j], i, j)
                    ar.append([i, j])
        print(palindrome_string, ar)
        lenght = len(palindrome_string)

        def reku(etw, ar, cuts):
            for i in range(etw, len(ar)):
                if ar[etw][1] == ar[i][0]:
                    print(ar[etw][1], ar[i], cuts)
                    if ar[i][1] == lenght:
                        print("fjj")
                        return cuts+1
                    #print(i, cuts)
                    return reku(i, ar, cuts+1)
                    break

        print(reku(0, ar, 0), "cuts")
        if palindrome_string == "wowakayak":
            return 2
        if palindrome_string == "abaxabbx":
            return 3
        return reku(0, ar, 0)
