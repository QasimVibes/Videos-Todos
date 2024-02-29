import sqlite3


con= sqlite3.connect("youtube_videos.db")
cur=con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    ) 
""")



def list_all_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    if len(rows) < 1:
        print("\nData not exists\n")
    else:
        print("*" * 70)
        for row in rows:
            print(f"{row[0]}. {row[1]}, and Duration is {row[2]}")
        print("*" * 70)



def add_new_video(name,time):
    cur.execute("INSERT INTO videos(name,time) VALUES(?, ?)",(name,time))
    con.commit()
    print("\nVideos add successfully\n")
    


def Update_video_details(id,name,time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?",(name,time,id))
    con.commit()
    print("\nUpdate video successfully")



def delete_video(delete_id):
    cur.execute("DELETE FROM videos WHERE id=?", (delete_id,)) # reminder
    con.commit()
    print("\nVideo delete successfully!\n")



def main():
    while True:
        print("\nYoutube Manager")
        print("1. List all youtube videos")
        print("2. Add a new video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exist The app")
        choices=input("Enter your choices:\n")

        match choices:
            case "1":
                list_all_videos()
            case "2":
                name=input("\nEnter your video name\n")
                time=input("\nEnter your video time\n")
                add_new_video(name,time)
            case "3":
                list_all_videos()
                id=int(input("\nEnter your video id\n"))
                name=input("\nEnter your updated video name\n")
                time=input("\nEnter your updated vidoe time\n")
                Update_video_details(id,name,time)
            case "4":
                list_all_videos()
                delete_id=int(input("\nEnter your delete video id\n"))
                delete_video(delete_id)
            case "5":
                print("\nProgram exit successfully\nThank you!")
                break 
            case _:
                print("\nInvalid number")
    con.close()
    
if __name__ == "__main__":
    main()