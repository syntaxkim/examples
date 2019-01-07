import requests

# In general, HTTP methods are used when dealing with API.
# For example, 'GET' request corresponds to retreiving resource.
# 'Post' request to creating new resource.
# And to easily use that HTTP methods in Python, you can use a 'requests' library.

def main():
    # res just stands for response
    res = requests.get("https://google.com")
    print(res, '\n')
    print(res.status_code, '\n')
    print(res.text, '\n')

if __name__ == "__main__":
    main()