from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
currrent_page = None

# visit function
NoOfvisists = int(input("Enter the number of url history: "))

print("Enter URLs to visit:")
for i in range(NoOfvisists):
    url = input("URL")
    print(f"visiting {url}")
    backward_history.put(currrent_page)
    current_page = url

 #Display current page
    print(f"Current page: {current_page}")

#Go back
while input("Do you want to go back? (yes/no): ").lower() == "yes":
  if not backward_history.empty:
    forwarrd_history.put(current_page)
    current_page = backward_history.get()
    print(f"Going back to {current_page}")
  else:
    print("No previous page avaliable")

#Go forward
while input("Do you want to go forward? (yes?/no): ").lower() =="yes":
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else: 
        print("No forward page available")