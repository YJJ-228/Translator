import win32clipboard
import time

def get_selected_text():
    time.sleep(1)
    win32clipboard.OpenClipboard()
    try:
        selected_text = win32clipboard.GetClipboardData()
    except TypeError:
        selected_text = ""
    win32clipboard.CloseClipboard()
    return selected_text

if __name__ == "__main__":
    pivort=''
    while True:
        selected_text = get_selected_text()
        if(selected_text!=pivort and selected_text!=''):
            pivort=selected_text
            print("复制的文本:", selected_text)
        elif(selected_text==pivort):
            time.sleep(1)
