import requests 
import json 

# 全局变量（用于存储获取到的用户数据、用户帖子数据）
users = []
user_posts = []
current_user = {}

def menu():
    print("Menu:")
    print("1. View all users")
    print("2. View selected user")
    print("3. View selected user's posts")
    print("4. Exit")
    # 修正：添加返回值，将用户选择返回给主循环
    choice = int(input("Input your choice: "))
    return choice

def display_users():
    # 先判断是否获取到了用户数据
    if not users:
        print("No user data available, please check your network or try again later.")
        return
    print("All users:")
    print("-"*11)
    for index, user in enumerate(users, 1): 
        if "id" in user and "name" in user:
            print(f"{index}. Name: {user['name']}, Id: {user['id']}")

def display_user_details(id_choice):
    # 先判断是否获取到了用户数据
    if not users:
        print("No user data available, please check your network or try again later.")
        return
    print("User details:")
    print("-"*11)
    # 修正1：逻辑错误 - 原代码判断 "id_choice in user" 是判断是否存在该键，不是值匹配
    # 修正2：添加标记，判断是否找到对应ID的用户
    user_found = False
    global current_user  # 声明使用全局变量，存储当前选中的用户
    for user in users:
        if "id" in user and user["id"] == id_choice:
            current_user = user  # 保存当前用户，方便后续帖子查询使用
            print(f"Name: {user['name']}")
            print(f"Id: {user['id']}")
            print(f"Email: {user['email']}")
            print("Address:")
            print(f"  Street: {user['address']['street']}")
            print(f"  City: {user['address']['city']}")
            print(f"  Zipcode: {user['address']['zipcode']}")
            user_found = True
            break
    if not user_found:
        print(f"User with ID {id_choice} not found.")

def fetch_user_posts(id_choice):
    # 修正1：声明使用全局变量 user_posts，用于存储获取到的帖子数据
    global user_posts
    # 先清空上一次的帖子数据，避免混淆
    user_posts = []
    try:
        post_response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={id_choice}", timeout=5)
        post_response.raise_for_status()
        user_posts = post_response.json()  # 赋值给全局变量，供后续展示使用
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def display_user_posts():
    # 先判断是否获取到了帖子数据
    if not user_posts:
        print("No post data available for this user.")
        return
    print("User posts")
    print("-"*11)
    # 修正：使用全局变量 current_user 显示用户名，避免语法错误
    print(f"Posts by {current_user.get('name', 'Unknown User')}:")
    # 修正：enumerate 从 1 开始，更符合用户使用习惯
    for index, post in enumerate(user_posts, 1):
        print(f"{index}. {post['title'][:30]}...")
    
    # 修正：增加输入合法性判断，避免非数字输入报错
    while True:
        try:
            view = int(input("View full post? (enter 0 for no, 1 for yes): "))
            break
        except ValueError:
            print("Invalid input, please enter 0 or 1.")
    
    if view == 1:
        # 修正：让用户选择查看哪一篇完整帖子（原代码直接显示最后一篇，逻辑有误）
        while True:
            try:
                post_index = int(input(f"Enter post number (1-{len(user_posts)}): ")) - 1
                if 0 <= post_index < len(user_posts):
                    selected_post = user_posts[post_index]
                    print(f"\nTitle: {selected_post['title']}")
                    print(f"Body: {selected_post['body']}")  # 原代码只显示前50字符，可保留也可完整显示
                    break
                else:
                    print(f"Invalid post number, please enter a number between 1 and {len(user_posts)}.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
    # 修正：移除原代码中的 menu() 调用，主循环已负责显示菜单，避免嵌套循环混乱

# ---------------------- 程序入口 ----------------------
print("Welcome to reminisce's api fetcher!")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    users = response.json()  # 赋值给全局变量 users，供其他函数调用
except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# 主循环
while True:
    # 修正：接收 menu() 函数的返回值，赋值给 choice
    choice = menu()
    
    if choice == 1:
        display_users()

    elif choice == 2:
        # 修正：增加输入合法性判断
        while True:
            try:
                id_choice = int(input("Enter user id: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number for user ID.")
        display_user_details(id_choice)

    elif choice == 3:
        # 修正：增加输入合法性判断
        while True:
            try:
                id_choice = int(input("Enter user id: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid number for user ID.")
        fetch_user_posts(id_choice)
        display_user_posts()
        
    elif choice == 4:  # 修正：明确匹配 4 退出，避免非法输入直接退出
        print("Thanks for using reminisce's api fetcher")
        break
    
    else:  # 处理 1-4 之外的非法选择
        print("Invalid choice, please enter a number between 1 and 4.")
    
    # 增加分隔线，优化输出格式
    print("\n" + "-"*30 + "\n")
