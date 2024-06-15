import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker_number = 1
vcs = speaker.GetVoices()
speaker.voice
speaker.SetVoice(vcs.Item(speaker_number))

lis = ["alameen", "interviewrs", "github"]
for names in lis:
    speaker.speak(f"shoutout to {names}")
print("shoutout has done")
