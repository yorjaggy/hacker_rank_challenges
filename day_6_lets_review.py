# Enter your code here. Read input from STDIN. Print output to STDOUT

def do(word):
    odd_letters = ""
    even_letters = ""
    for i in range(len(word)):
        if i%2==0:
            even_letters = even_letters+word[i]
        elif i%2==1:
            odd_letters = odd_letters+word[i]

    return "{} {}".format(even_letters,odd_letters)

if __name__ == "__main__" :
    num = int(input())
    for x in range(num):
        word = input()
        print(do(word))