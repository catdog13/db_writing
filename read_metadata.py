import subprocess


def converter(path, status):
    ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
    path_without = path.strip(".mp4")
    if status:
        args = ' -hide_banner -i "' + path + \
            '" -metadata comment="Watched" ' \
            '-metadata title="" -strict experimental ' \
            '-map 0:0 -c:v copy ' \
            '-map 0:1 -c:a copy "' \
            + path_without + '2.mp4"'
    else:
        args = ' -hide_banner -i "' + path + \
            '" -metadata comment="Unwatched" ' \
            '-metadata title="" -strict experimental ' \
            '-map 0:0 -c:v copy ' \
            '-map 0:1 -c:a copy "' \
            + path_without + '2.mp4"'

    process = ffmpeg_path + args
    print(process)
    subprocess.Popen(process, stdout=subprocess.PIPE).stdout.read()

converter(r"C:\Users\Tom\Documents\GitHub\un-watched_status\Not Another Happy Ending.mp4", False)
converter(r"C:\Users\Tom\Documents\GitHub\un-watched_status\Men In Black 3.mp4", True)
converter(r"C:\Users\Tom\Documents\GitHub\un-watched_status\Against the Wild.mp4", True)
converter(r"C:\Users\Tom\Documents\GitHub\un-watched_status\The Perfect Wave.mp4", True)
converter(r"C:\Users\Tom\Documents\GitHub\un-watched_status\History of the World Part I.mp4", True)
