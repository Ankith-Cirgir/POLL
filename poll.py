import sys, sqlite3


def status(c):
    conn = c.cursor()
    conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name="POLL" ''')

    if conn.fetchone()[0]==0 : 
        print("No VOTES to show!")
        sys.exit()


    conn.execute(''' SELECT count(*) FROM POLL ''')
    n = conn.fetchone()[0]

    conn.execute("""  SELECT count(*) FROM POLL WHERE VOTE="1" """)
    option1 = conn.fetchone()[0]
    conn.execute("""  SELECT count(*) FROM POLL WHERE VOTE="2" """)
    option2 = conn.fetchone()[0]
    conn.execute("""  SELECT count(*) FROM POLL WHERE VOTE="3" """)
    option3 = conn.fetchone()[0]
    conn.execute("""  SELECT count(*) FROM POLL WHERE VOTE="4" """)
    option4 = conn.fetchone()[0]
    

    print(f"Total number of votes: {n}")
    print(f"Number of votes for option 1: {option1} ({round((option1/n)*100,2)}%)")
    print(f"Number of votes for option 2: {option2} ({round((option2/n)*100,2)}%)")
    print(f"Number of votes for option 3: {option3} ({round((option3/n)*100,2)}%)")
    print(f"Number of votes for option 4: {option4} ({round((option4/n)*100,2)}%)")


def check(c,name):
    conn = c.cursor()
    conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name="POLL" ''')

    if conn.fetchone()[0]==0 : 
        conn.execute('''CREATE TABLE POLL
            (ID INTEGER PRIMARY KEY,
            NAME           TEXT    NOT NULL,
            VOTE            INT     NOT NULL);''')

    conn.execute(f''' SELECT count(name) FROM POLL WHERE name='{name}' ''')
    if conn.fetchone()[0]==1:
        print("you already casted your vote!")
        sys.exit()
    else:
        return


def upload(c,var,name):
    conn = c.cursor()

    conn.execute(f'INSERT INTO POLL(NAME, VOTE) VALUES (?,?)',(name,var))
    c.commit()


conn = sqlite3.connect('test.db')
if(len(sys.argv) >=2):
    if(sys.argv[1] == "status"):
        status(conn)
        sys.exit()
    else:
        print("Unknown ARGUMENT passed")
        sys.exit()

print("Enter your name: ",end="")
name = input()
check(conn,name)


print("Question: What’s the strangest thing you did while attending a meeting online?")
print("1)Ate breakfast")
print("2)Brushed my teeth")
print("3)Watched Netflix")
print("4)Actually paying attention to the meeting")

print("\n Choose any option...(legit answers only)")

n = int(input())
upload(conn,n,name)
#status(conn)
print("Casted your vote Successfully !")
