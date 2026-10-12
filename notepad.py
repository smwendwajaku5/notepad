def new_note():
    print("\n----------New Note--------")
    note = input("Write your note (end with a single line'END'):\n")
    lines = []
    while True :
        line = input()
        if line == 'END':
            break
        lines.append(line)
        note = "\n".join(lines)
        return note

def view_note(note):
    print("\n-----------------Your Note----------------")
    if note.strip() == "":
        print("No Note to Display.")
    else:
        print(note)

def save_note(note):
    filename = input("Enter filename to save(e.g. Note.txt):")

    try:
        with open(filename, 'w', encoding='utf-8') as file :
            file .write(note)
        print(f"Note saved successfully in '{filename}'")
    except Exception as e :
        print("Error saving note:", e)

def main():
    note =""
    while True:
        print("\n=============NOTEPAD APP===========")
        print("1.New Note\n2. View Note \n3. Save Note \n4. Exit ")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            note = new_note()
        elif choice == '2':
            view_note(note)
        elif choice =='3':
            save_note(note)
        elif choice =='4':
            print("GOODBYE!!!!!")
        else:break
        print("Invalid choice Try again. ")

if __name__== "__main__":
    main()


        
        
        