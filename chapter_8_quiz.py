# 8-3 T-Shirt
def make_shirt(text, size='L'):
    
    if size == "L":
        print("\nThe size of the shirt is " + size + "." +
              " Print on shirt: " + text)
    elif size == "M":
        print("Your " + size + " shirt: #I love python - added to cart")
    else:
        print("no shirts are available for you")
make_shirt('#Stop Shazaming my tracks!', 'M')
