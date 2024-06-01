def bark():
  name = input("Enter the dog's name: ").capitalize()
  age = input("Enter the dog's age: ")
  breed = input("Enter the dog's breed: ").capitalize()
  print(f"{name}, the {age} year old {breed}, says, \"Woof!\"")

def bark_with_validation():
  valid_breeds = ["Schnauzer", "Terrier", "Poodle", "Mastiff"]
  name = input("Enter the dog's name: ")
  if not name.isalpha() or len(name) < 2:
    print("Name error!")
    return
  age = input("Enter the dog's age: ")
  if not age.isdigit() or not (0 <= int(age) <= 15):
    print("Age error!")
    return
  breed = input("Enter the dog's breed: ")
  if breed.capitalize() not in valid_breeds:
    print("Breed error!")
    return
  print(f"{name.capitalize()}, the {age} year old {breed.capitalize()}, says, \"Woof!\"")

def respond_to_anything():
  sentence = input("Input a sentence: ")
  if sentence.endswith('.'):
    print("That's true.")
  elif sentence.endswith('?'):
    print("I'm sorry, I don't know.")
  elif sentence.endswith('!'):
    print("Exciting!")
  else:
    print("Please include a punctuation mark at the end of your sentence!")

def respond_to_anything_but_nonsense():
  sentence = input("Input a sentence: ")
  if 'nonsense' in sentence.lower():
    return
  if sentence.endswith('.'):
    print("That's true.")
  elif sentence.endswith('?'):
    print("I'm sorry, I don't know.")
  elif sentence.endswith('!'):
    print("Exciting!")
  else:
    print("Please include a punctuation mark at the end of your sentence!")
