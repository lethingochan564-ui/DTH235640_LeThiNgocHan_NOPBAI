
def get_filename(path):
    return path.split("\\")[-1].split("/")[-1]

def get_filename_no_ext(path):
    filename = get_filename(path)
    dot_index = filename.rfind(".")
    if dot_index != -1:
        return filename[:dot_index]
    return filename 

path = "d:\\music\\muabui.mp3"
print("Đường dẫn:", path)
print("Tên file  :", get_filename(path))
print("Không đuôi:", get_filename_no_ext(path))