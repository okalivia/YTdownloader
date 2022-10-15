# YTdownloader
#### Download videos or playlists (mp3 or mp4) from Youtube

### Installation

Install dependencies :

- ``pip install pytube``
        
- ``pip install moviepy``
        
or
        
- ``python.exe -m pip install pytube``
        
- ``python.exe -m pip install moviepy``

### How to use

    YTdownloader.py [-h] -l LINK -p PATH [-a]

    options:
      -h, --help            show this help message and exit
      -l LINK, --link LINK  Enter the youtube video or playlist link without any & symbol
      -p PATH, --path PATH  Enter the path to store video(s)
      -a, --audio           Download only the audio, without video
 
### Examples :

Print Help
> YTdownloader.py -h

Download a single video (mp4)
> YTdownloader.py -l https://www.youtube.com/watch?v=dQw4w9WgXcQ -p Videos

Download a single video in mp3 (audio only)
> YTdownloader.py -l https://www.youtube.com/watch?v=dQw4w9WgXcQ -p .\Music -a

Download a playlist with videos (mp4)
> YTdownloader.py -l https://www.youtube.com/playlist?list=PLkezPydZpc2ugdWVtom4gyRrE9T1F1rR6 -p .\Videos\FrenchSongs

Download a playlist in mp3 (audio only)
> YTdownloader.py -l https://www.youtube.com/playlist?list=PLkezPydZpc2ugdWVtom4gyRrE9T1F1rR6 -p ./Music/MyPlaylist80 -a
