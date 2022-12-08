from moviepy.editor import *


class EditAudio:
    videoName = ""
    timestamp = []

    def __init__(self, videoName, times):
        self.videoName = videoName
        self.timestamp = times
        try:
            self.video = VideoFileClip(videoName)
        except Exception as IO:
            print("Not detection")

    def getOriginalAudio(self, videoclip):
        return videoclip.audio

    '''
    function name : getTTS
    do : make a list to save TTS file names, list length is count of TTS files
    param :
        len - TTS file list coun
    '''

    def getTTS(self, items):
        TTS_audio = []
        for i in items:
            TTS_audio.append(AudioFileClip("../TTS/kor_FAST" + str(i+1) + ".wav"))
        return TTS_audio

    def getTimestamp(self, timestamp):
        return self.timestamp

    '''
    function name : setAudio
    do : edit audio file with TTS list
    param :
        audio - original audio file
        tts - tts file list (getTTS())
        timestamp - time list to insert TTS (getTimestamp())
    * test needed
    '''

    def setAudio(self, audio, tts, timestamp):
        for i in range(len(timestamp)):
            # result = CompositeAudioClip([audio.set_start(i), tts]) # 오디오 합성하기
            audio = CompositeAudioClip([tts[i].set_start(timestamp[i]), audio])  # 오디오 합성하기
        return audio

    # setAudio(getOriginalAudio(), getTTS(), getTimestamp())

    '''
    function name : setVideo
    do : make final video with edited audio
    param :
        name - video name for making
        audio - edited audio file (setAudio())
        video - original video to composite
    '''

    def setVideo(self, name, audio, video):
        video.audio = audio
        # result name?
        video.write_videofile("result.mp4")
        print("Video production succeeded")
        return video
    # setVideo(name, setAudio(), getVideo())
