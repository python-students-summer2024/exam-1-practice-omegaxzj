def weather_helper():
  temp = int(input("Enter the current temperature in degrees Fahrenheit: "))
  if not (-70 <= temp <= 134):
    print("Invalid temperature!")
    return

  affirmative_responses = {"yes", "yeah", "yup"}

  if temp < 40:
    if input("Is it snowing? (yes/no): ").lower() in affirmative_responses:
      if input("Are you wearing a warm jacket? (yes/no): ").lower() in affirmative_responses:
        print("Glad to hear you're dressed appropriately!")
      else:
        print("What were you thinking when you left home today?!")
    else:
      if input("Is it raining? (yes/no): ").lower() in affirmative_responses:
        if input("Do you have an umbrella? (yes/no): ").lower() in affirmative_responses:
          print("Good job staying dry!")
        else:
          print("You must enjoy getting wet!")
  elif temp > 90:
    if input("Do you have air conditioning? (yes/no): ").lower() in affirmative_responses:
      print("Stay cool indoors.")
    else:
      print("I hope you have a fan.")

