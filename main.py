import gdshortener
import time, requests, json
s = gdshortener.ISGDShortener()
varlogstat = True

print("Welcome to this URL Shortner! This programme helps you to make a Short URL.")
time.sleep(0.2)
print("What would you like to do?")
time.sleep(0.2)
print('1 - Shorten a URL') 
time.sleep(0.2)
print('2 - Make a custom short URL')
time.sleep(0.2)
print("3 - Check what a URL is")
time.sleep(0.2)
print("4 - Settings")
time.sleep(0.3)
choice = str(input("Enter your command: "))


try: 
  if choice == '1': 
    print("Now enter the URL you want to shorten.")
    print("FAQ: https://is.gd/faq.php")
    longurl = input(">>")
    url = requests.get(f"https://is.gd/create.php?format=json&url={longurl}")
    text = url.text
    data = json.loads(text)
    urldata = data
    print(data['shorturl'])
    
  elif choice == '2':
    try:
      print("Now enter the URL you want to shorten.")
      print("FAQ: https://is.gd/faq.php")
      longurl2 = input(">>")
      print("Enter the latter part of the URL")
      custom = input(">>")
      url = requests.get(f'https://is.gd/create.php?format=json&url={longurl2}&shorturl={custom}')
      text = url.text
      data = json.loads(text)
      urldata = data
      print(data['shorturl'])
    except:
      print('The link is occupied. Please try again.')
  elif choice == "3":
    print("Enter the URL you want to reverse search.")
    reverse = input(">>")
    print("The URL",reverse,"redirects to",s.lookup(f'{reverse}'))
  elif choice == '4':
    print("Sorry, settings don't work yet. We are working to push it in the next update. ")
    #What setting do you want to change?\n1 - Enable logging statistics\n2- Disable logging statistics \n3- Ingore the SSL Certificate (not reccomended, only for older versions of OpenSSL)\n4 - Use SSL
    
  else:
    print('Please enter the correct command. Currently all links:\n - Do not log statistics \n - Have SSL enabled')
except:
  print('Error')
