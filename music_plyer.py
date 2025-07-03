# music player library

import os
import vlc
import time
import random
import threading
import speaker
import music_list

# MediaPlayer class
class MediaPlayer:
    # setup for playing music
    def __init__(self, song_dict):
        self.song_dict = song_dict
        self.song_names = list(song_dict.keys())
        self.player = None
        self.current_index = 0
        self.playing = False
        self.shuffle = False
        self.stack = []

        # Start background thread to monitor player state
        self.monitor_thread = threading.Thread(target=self._monitor_player)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    #function which plays music 
    def play(self, index=None):
        if index is not None:
            self.current_index = index

        if not self.song_names:
            print("Playlist is empty.")
            return

        self._stop_if_playing()
        song_name = self.song_names[self.current_index]
        file_path = self.song_dict[song_name]
        self.player = vlc.MediaPlayer(file_path)
        self.player.play()
        self.playing = True
        print(f"▶ Playing: {os.path.basename(song_name)}")
        speaker.speak(f"Playing: {os.path.basename(song_name)}")

    # function which pauses music
    def pause(self):
        if self.player:
            self.player.pause()
            print("⏸ Paused")
            speaker.speak("Paused")
    
    # function which resumes music
    def resume(self):
        if self.player:
            state = self.player.get_state()
            if state == vlc.State.Paused:
                self.player.pause()  # Calling pause() again resumes playback
                print("▶ Resumed")
                speaker.speak("Resumed")
            else:
                print("⚠ Not paused — can't resume.")
                speaker.speak("Not paused — can't resume.")

    # function which stops the music
    def stop(self):
        if self.player:
            self.player.stop()
            self.playing = False
            print("⏹ Stopped")
            speaker.speak("Stopped")

    # function to play next song
    def next_song(self):
        if not self.song_names:
            return
        
        if(self.shuffle == False):
            self.current_index = (self.current_index + 1) % len(self.song_names)
            self.play(self.current_index)
        else:
            self.current_index = random.randint(0, len(self.song_names) - 1)
            self.stack.append(self.current_index)
            self.play(self.current_index)

    # function to play previous song
    def prev_song(self):
        if not self.song_names:
            return
        if(self.shuffle == False):
            self.current_index = (self.current_index - 1) % len(self.song_names)
            self.play(self.current_index)
        else:
            try:
                self.current_index = self.stack.pop()
                self.play(self.current_index)
            except IndexError:
                print("no previous songs")
                self.current_index = (self.current_index - 1) % len(self.song_names)
                self.play(self.current_index)

    # function to turn on-off the shuffle mode
    def shuffle_songs(self):
        if(self.shuffle == True):
            self.shuffle = False
            speaker.speak("shuffle off")
        else:
            self.shuffle = True
            speaker.speak("shuffle on")

    # function to play song by name takes name of song as input
    def play_by_name(self, name):
        if name in self.song_dict:
            self.current_index = self.song_names.index(name)
            self.play(self.current_index)

    # stop the current playing song
    def _stop_if_playing(self):
        if self.player and self.player.is_playing():
            self.player.stop()

    # function to play the next song if current song is completed
    def _monitor_player(self):
        while True:
            if self.player and self.playing:
                state = self.player.get_state()
                if state == vlc.State.Ended:
                    print("🎵 Song finished. Playing next...")
                    self.next_song()
            time.sleep(5)

    # function to show all the songs of the playlist
    def show_playlist(self):
        print("🎵 Playlist:")
        for i, song in enumerate(self.song_names):
            print(f"{i + 1}. {os.path.basename(song)}")


music_folder = r"D:\songs\Music(eng)"  # <- update this path

player = MediaPlayer(music_list.eng_music)
