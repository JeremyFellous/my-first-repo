print("1. + 2. ")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Don't divide by zero" + str(e.args))

print("3. ")

try:
    x = 1
finally:
    print("finally")
# We can see that this code is legal.

# 4.
# except can handle to all type of exceptions.

# 5.
# this type of exception handler catches all type of exceptions,
# what is wrong about it is you are losing valuable information about the type of exception being thrown.

# 6.
# The IOError handler for Windows error.
# The ZeroDivisionError handler dor division by zero.

# 7.
my_file = open("words.txt", 'w')
my_file.close()

# 8.
my_file = open("words.txt", 'a')
my_file.write("Jeremy" + "\n")
my_file.close()

print("9. ")

my_file = open("words.txt", 'r', encoding='utf-8')
words = my_file.read()
print(words)
my_file.close()

print("10. ")

my_file = open("words.txt", "a", encoding='utf-8')
my_file.write("שלום לכולם" + "\n")
my_file.close()

my_file = open("words.txt", "r", encoding='utf-8')
print(my_file.read())
my_file.close()

print("11.Flask")

from flask import Flask
app = Flask(__name__)


@app.route('/content')
def content():
    my_file = open("words.txt", 'r')
    return my_file.read(), 200


@app.route('/register')
def register():
    with open("words.txt", 'w') as my_file:
        my_file.write("hello")
    return "success", 201


if __name__ == '__main__':
    app.run('0.0.0.0', port=30000, debug=True)

# print("Challenge: ")

from PIL import Image

img = Image.new('RGB', (60, 30), color='red')
img.show()





