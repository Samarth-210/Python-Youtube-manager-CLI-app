import json
import sys

def list_all_videos(videos):
    print("\n")
    print("*" *70)
    if not videos:
        print("No videos found.")
    else:
       for index,video in enumerate(videos,start=1):
          print(f"{index}. {video['name']} , Duration: {video['time']}")

    print("*" *70)
    sys.stdout.flush()  # Flush the output buffer to ensure the prompt is displayed immediately

def add_video(videos):
    name = input("Enter video name: ")
    time=input("Enter video time:")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def main():

        videos=load_data()

        while True:
            print("\n Youtube manager | choose an option")
            print("[1] List all youtube videos")
            print("[2] Add a new youtube video")
            print("[3] Update a youtube video")
            print("[4] Delete a youtube video")
            print("[5] Exit the app")
             # Flush the output buffer to ensure the prompt is displayed immediately
            choice=input("Enter your choice: ").strip()
            
            match choice:#Similar to switch case in other languages
                case '1':
                    list_all_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    update_video(videos)
                case '4':
                    delete_videos(videos)
                case '5':
                    break
                case _:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()