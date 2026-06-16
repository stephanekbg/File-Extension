def main():
    
    # The Rules and Logic for the 
    # program areon the README file
    
    # Getting user input 
    # .lower() : to make it case incesitive
    filename = input("input: ").lower().strip()
    
    
    # let's build the logic
    # we can use conditionals
    # or use cases
    # let's use conditionals this one time
    
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        print("image/jpeg")
    elif filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".zip"):
        print("application/zip")
    elif filename.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")
        
        
    
    
    
main()