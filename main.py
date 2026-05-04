import subprocess

STREAM_URL = "https://backup.qurango.net/radio/mishary_rashid"
RTMP_URL = "rtmps://dc4-1.rtmp.t.me/s/3918211293:8W57IADAF82v8kMEfVSOAw"

cmd = [
    "ffmpeg", "-re",
    "-i", STREAM_URL,
    "-vn",
    "-acodec", "aac",
    "-ab", "128k",
    "-ar", "44100",
    "-f", "flv",
    RTMP_URL
]

subprocess.run(cmd)
