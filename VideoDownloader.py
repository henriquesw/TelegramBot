from pytube import YouTube

class VideoDownloader:
    def __init__(self, url):
        self.url = url
        self.path = './Videos/'
        self.yt = None
        self.video = None
        self.openVideo()

    def openVideo(self):
        try:
            self.yt = YouTube(self.url)
            self.video = self.yt.streams.filter(file_extension='mp4').order_by('resolution').last()
        except:
            print(f'Video {self.url} is unavaialable, skipping.')

    def getVideoName(self):
        if self.video == None:
            return 'Error to access video'   
        else: 
            return "Downloading " + self.video.title

    def downloadVideo(self):
        if(self.video != None):
            self.video.download(self.path)
            return self.path + self.video.default_filename