# What should I wear?"
temp = int(input('Please enter the temperature in Celsius. An integer between 0-40:>>> '))

if temp > 30:
    print('Wear shorts and sun cream!')
elif temp <= 30 and temp > 20:
    print('It\'s warm but not hot enough to wear shorts')
elif temp <= 20 and temp > 10:
    print('It\'s cold outside! Wear a jacket')
else:
    print('Too cold! Stay inside!')
