
# Homework 1. ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False 

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Bajardi" if self.completed else "❌ Bajarmagan"
        return f"Nomi: {self.title} | Tavsif: {self.description} | Muddat: {self.due_date} | Holat: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        if not self.tasks:
            print("📭 Vazifalar yo‘q.")
            return
        print("\n📋 Barcha vazifalar:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        print("\n❌ Bajarmagan vazifalar:")
        found = False
        for i, task in enumerate(self.tasks, start=1):
            if not task.completed:
                print(f"{i}. {task}")
                found = True
        if not found:
            print("🎉 Hamma vazifalar bajarilgan!")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Vazifa bajarildi deb belgilandi.")
        else:
            print("⚠️ Xato: Noto‘g‘ri raqam.")

def main():
    todo = ToDoList()

    while True:
        print("\n===== TO DO LIST MENU =====")
        print("1. Vazifa qo‘shish")
        print("2. Barcha vazifalarni ko‘rish")
        print("3. Faqat bajarmagan vazifalarni ko‘rish")
        print("4. Vazifani bajarilgan deb belgilash")
        print("5. Dasturdan chiqish")

        choice = input("Tanlovingiz (1-5): ")

        if choice == "1":
            title = input("Vazifa nomi: ")
            description = input("Tavsif: ")
            due_date = input("Muddat (yyyy-mm-dd): ")
            new_task = Task(title, description, due_date)
            todo.add_task(new_task)
            print("✅ Vazifa muvaffaqiyatli qo‘shildi.")
        elif choice == "2":
            todo.list_all_tasks()
        elif choice == "3":
            todo.list_incomplete_tasks()
        elif choice == "4":
            todo.list_all_tasks()
            try:
                task_num = int(input("Qaysi vazifa raqamini bajarildi deb belgilaysiz? ")) - 1
                todo.mark_task_complete(task_num)
            except ValueError:
                print("⚠️ Raqam kiriting.")
        elif choice == "5":
            print("👋 Dastur yakunlandi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")

if __name__ == "__main__":
    main()








#  Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"\n📌 Sarlavha: {self.title}\n✍️ Muallif: {self.author}\n📝 Kontent:\n{self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("📭 Postlar mavjud emas.")
            return
        print("\n📚 Barcha postlar:")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post}")

    def display_posts_by_author(self, author_name):
        print(f"\n🔎 Muallif bo‘yicha qidiruv: {author_name}")
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print("⚠️ Bu muallifga tegishli post topilmadi.")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            deleted = self.posts.pop(index)
            print(f"🗑️ Post '{deleted.title}' o‘chirildi.")
        else:
            print("⚠️ Xato: Noto‘g‘ri post raqami.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
            print("✏️ Post muvaffaqiyatli tahrirlandi.")
        else:
            print("⚠️ Xato: Noto‘g‘ri post raqami.")

    def latest_posts(self, count=3):
        print(f"\n🆕 Eng so‘nggi {count} ta post:")
        for post in self.posts[-count:]:
            print(post)



def blog_main():
    blog = Blog()

    while True:
        print("\n====== BLOG MENYU ======")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. So‘nggi postlarni ko‘rish")
        print("7. Chiqish")

        choice = input("Tanlovingiz (1-7): ")

        if choice == "1":
            title = input("Post sarlavhasi: ")
            content = input("Post kontenti: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("✅ Post qo‘shildi.")
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author_name = input("Muallif ismini kiriting: ")
            blog.display_posts_by_author(author_name)
        elif choice == "4":
            blog.list_posts()
            try:
                index = int(input("Qaysi post raqamini o‘chirasiz? ")) - 1
                blog.delete_post(index)
            except ValueError:
                print("⚠️ Raqam kiriting.")
        elif choice == "5":
            blog.list_posts()
            try:
                index = int(input("Qaysi postni tahrirlaysiz (raqam)? ")) - 1
                new_title = input("Yangi sarlavha: ")
                new_content = input("Yangi kontent: ")
                blog.edit_post(index, new_title, new_content)
            except ValueError:
                print("⚠️ Raqam kiriting.")
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            print("👋 Dastur tugatildi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov.")


if __name__ == "__main__":
    blog_main()




#Project 3 

# Project -- Banking Project
# Tool -- Python class
# Account, Bank
import datetime

class Account:
    def __init__(self,holder_name):
        opened_date = datetime.datetime.today()
        self.holder_name = holder_name
        self.opened_date = opened_date
        self.id = 0
        self.balance = 0
        self.closed_date = None
    def deposit_money(self,deposit):
        self.balance += deposit
        return self.balance
    def withdraw_money(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            return True
        return False
    def close_account(self):
        self.closed_date = datetime.datetime.today()
    def __str__(self):
        return f"Account Number: {self.id} | Holder Name: {self.holder_name} | Balance: {self.balance}"
    

class Bank:
    account_list = []
    last_id = 0
    def __init__(self,name):
        self.name  = name
    def add_account(self):
        self.last_id += 1
        holder_name = input("Enter Your Name: ")
        account_obj = Account(holder_name)
        account_obj.id = self.last_id
        self.account_list.append(account_obj)
        print(f"Acccount Number {self.last_id} was added successfully")
    def search(self,id):
        for obj in self.account_list:
            if obj.id == id:
                return obj
        return False
    def deposit_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            deposit_amount = int(input("Enter your deposit amount! ex: 1000$ 💸 "))
            balance = a.deposit_money(deposit_amount)
            print(f"Depositing Process is completed successfully | Current Balance: {balance}")
        else:
            print(f"Account Number {id} is not found")
    def withdraw_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            withdraw_amount = int(input("Enter withdraw amount "))
            result = a.withdraw_money(withdraw_amount)
            if result:
                print(f"The withdraw process completed successfully! withdraw Amount: {withdraw_amount} | Current Balance: {a.balance}")
            else:
                print(f"Your account has not available amount! Amount: {withdraw_amount} | Current Balance: {a.balance}")
    def show_accounts_details(self):
        for i in self.account_list:
            print(i)
    def show_specific_account(self,id):
        a =  self.search(id)
        print(a)
    def close_account(self,id):
        a = self.search(id)
        a.close_account()
        print(f"Account Number {a.id} is closed")

milly_bank = Bank('milliy bank')
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")



while True:
    print_menu()
    command = input("Enter a number: ")
    if command == '1':
        milly_bank.add_account()
    elif command == '2':
        milly_bank.show_accounts_details()
    elif command == '3':
        account_number = int(input("Enter account Number: "))
        milly_bank.deposit_account(account_number)
    elif command == '4':
        account_number = int(input("Enter account Number: "))
        milly_bank.withdraw_account(account_number)
    elif command == '5':
        account_number = int(input("Enter account Number: "))
        milly_bank.show_specific_account(account_number)
    else:
        exit()
