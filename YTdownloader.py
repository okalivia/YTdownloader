from pytube import YouTube, Playlist
import argparse, time, os
from moviepy.editor import VideoFileClip, AudioFileClip

# PARSE ARGUMENTS
parser = argparse.ArgumentParser(description='Download videos from Youtube')
parser.add_argument('-l', '--link', dest='link', required=True, help='Enter the youtube video or playlist link without any & symbol')
parser.add_argument('-p', '--path', dest='path', required=True, help='Enter the path to store video(s)')
parser.add_argument('-a', '--audio', dest='audio', required=False, action='store_true', help='Download only the audio, without video')
args = parser.parse_args()

# DEFINE VARS
path = args.path # Path to save
link = args.link # link of the video
audio_only = args.audio # audio or video

# DEFINE FUNCTIONS
def YTDownload(LINK, SAVE_PATH, AUDIO_ONLY):

	# TRY TO REACH PLAYLIST OR VIDEO
	try:
		# PLAYLIST PART
		if ("playlist?list=" in LINK): # if link is a playlist
			yt = Playlist(LINK)
			total = len(yt.video_urls) # count total of videos into the playlist
			count = 0

			# IF PLAYLIST IS REACHABLE
			if (total > 0): # if playlist is not empty (or private)
				print(f'\n\x1b[0;31;90m[>] {total} videos from \"{yt.title}\" playlist will be downloaded \x1b[0m\n')
				time.sleep(5)

				# REACH VIDEO BY VIDEO
				for video in yt.video_urls: # for each video
					count += 1
					yt2 = YouTube(video)
					print(f'\x1B[0;31;35m[*] {yt2.title} - {yt2.author}\x1b[0m') # video info
					audio = mp3(yt2)
					video = mp4(yt2) if not AUDIO_ONLY else False # if video is needed
					if (save(yt2.title, audio, video, SAVE_PATH)):
						print(f'\x1b[0;31;92m[{count}/{total}] Task completed \x1b[0m\n')

			# IF PLAYLIST IS EMPTY OR PRIVATE
			else:
				print(f'\n\x1b[6;31;40m Access Error : \x1b[0m')
				print(f'\x1b[6;31;40m Playlist is empty or private \x1b[0m\n')

		# SINGLE VIDEO PART
		else:
			yt = YouTube(LINK)
			print(f'\n[*] {yt.title} - {yt.author}') # video info
			audio = mp3(yt)
			video = mp4(yt) if not AUDIO_ONLY else False # if video is needed
			if (save(yt.title, audio, video, SAVE_PATH)):
				print(f'\n\x1b[0;31;92m[1/1] Task completed \x1b[0m\n')	

	# IF PLAYLIST OR VIDEO CANNOT BE REACHED
	except Exception as e:
		print(f'\n\x1b[6;31;40m Connection Error : \x1b[0m')
		print(f'\x1b[6;31;40m Youtube link seems not write correctly \x1b[0m')
		print(f'\x1b[6;31;40m [Detail] {e}\x1b[0m\n')

def mp4(YOUTUBE):
	settings = YOUTUBE.streams.filter(file_extension='mp4').order_by('resolution')
	settings = settings.last()
	return settings

def mp3(YOUTUBE):
	settings = YOUTUBE.streams.filter(only_audio=True)
	settings = settings.first()
	return settings

def save(FILENAME, AUDIO, VIDEO, SAVE_PATH):
	try:
		if (not VIDEO): # audio part
			AUDIO.download(filename=f"{FILENAME}.mp3", output_path=SAVE_PATH) # downloading the audio in mp3
		else:
			VIDEO.download(filename=f"temp_video.mp4", output_path=SAVE_PATH) # downloading the video
			AUDIO.download(filename=f"temp_audio.mp3", output_path=SAVE_PATH) # downloading the audio
			video_clip = VideoFileClip(f"{SAVE_PATH}/temp_video.mp4")
			audio_clip = AudioFileClip(f"{SAVE_PATH}/temp_audio.mp3")
			final_clip = video_clip.set_audio(audio_clip)
			final_clip.write_videofile(f"{SAVE_PATH}/{FILENAME}.mp4")
			os.remove(f"{SAVE_PATH}/temp_video.mp4")
			os.remove(f"{SAVE_PATH}/temp_audio.mp3")
		return True

	except Exception as e:
		print(f'\n\x1b[6;31;40m Save Error : \x1b[0m')
		print(f'\x1b[6;31;40m Path seems not to be correct \x1b[0m')
		print(f'\x1b[6;31;40m [Detail] {e}\x1b[0m\n')
		return False

# CALL MAIN FUNCTION
if __name__ == "__main__":
	YTDownload(link, path, audio_only)