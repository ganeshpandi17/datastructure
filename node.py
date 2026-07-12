class Song:
    def __init__(self,data):
        self.data=data
        self.next=None

class Playlist:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
   
    def append(self,data):
        new_song= Song(data)
        if self.head is None:
            self.head=new_song
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_song
   
    def prepend(self,data):
        new_song=Song(data)
        new_song.next=self.head
        self.head=new_song

    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
   
    def insert(self,data,prev):
        song=Song(data)
        current=self.head
        while current:
            if current.data==prev:
                song.next=current.next
                current.next=song
                return
            current=current.next
        return

    def Search(self,data):
        current=self.head
        while current:
            if current.data==data:
                print("Song",data,"available")
                return
            current=current.next
        print("Song ",data,"not available")
        return
   
    def display(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")
playlist=Playlist()
n=int(input("Enter the number of song"))
for i in range(n):
    s=input("Enter the song[i]")
    playlist.append(s)
print("New playlist")
playlist.display()
s0=input("Enter the new song")
playlist.prepend(s0)
print("\nAfter Prepend")
playlist.display()
i1=input("Enter the song to be inserted")
in_ne=input("Enter song before the inserted song")
playlist.insert(i1,in_ne)
print("\nAfter Insert")
playlist.display()
d1=input("Enter the song to be deleted")
playlist.delete(d1)
print("\nAfter Delete\n")
playlist.display()
se=input("Enter the song to be searched")
playlist.Search(se)
