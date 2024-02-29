import json

def list_all_videos(videos):
    print("\nAll youtube video lists\n")
    print("*" * 70)
    for key,value in enumerate(videos,start=1):
        print(f"{key}. {value["name"]}, Duration {value["time"]}")
    print("*" * 70)



def add_new_video(videos):
    name=input("\nEnter your videos name\n")
    time=input("\nEnter your videos time\n")
    videos.append({"name":name,"time":time})
    save_video_helper(videos)
    print("\nVideos add successfully\n")



def Update_video_details(videos):
    list_all_videos(videos)
    existing_video=input("Enter you video name which want to update\n")
    for video in videos:
        if video["name"]==existing_video:
            update_name=input("\nEnter your updated name\n")
            update_time=input("\nEnter your updated time\n")
            video["name"]=update_name
            video["time"]=update_time
            save_video_helper(videos)
            print("\nUpdate video successfully")
            break
    else:
        print("\nSorry! Your update video not in your list\n")
        


def delete_video(videos):
    list_all_videos(videos)
    delete=input("\nWhich video you want to delete\n")
    for key,value in enumerate(videos,start=0):
        if value["name"]==delete:
            videos.pop(key)
            save_video_helper(videos)
            print("\nVideo delete successfully!\n")  
            break
    else:   
        print("\nSorry! Your Deleting video not in your list\n")



def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



def save_video_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)



def main():
    videos=load_data()
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
                list_all_videos(videos)
            case "2":
                add_new_video(videos)
            case "3":
                Update_video_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("\nProgram exit successfully\nThank you!")
                break 
            case _:
                print("\nInvalid number")

if __name__ == "__main__":
    main()