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
playlist.append("Pavazha malli")
playlist.append("Nallaru poo")
playlist.append("Sakkarai Nilave ")
print("New playlist")
playlist.display()
playlist.prepend("Karupuu kooda vaa")
print("\nAfter Prepend")
playlist.display()
playlist.insert("Kannukulla","Nallaru poo")
print("\nAfter Insert")
playlist.display()
playlist.delete("Sakkarai Nilave")
print("\nAfter Delete\n")
playlist.display()
playlist.Search("Pavazha malli")
