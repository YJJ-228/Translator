import win32gui
import win32process
import time

def get_selected_text():
    hwnd = win32gui.GetForegroundWindow()
    tid, pid = win32process.GetWindowThreadProcessId(hwnd)
    win32gui.AttachThreadInput(win32gui.GetWindowTextLength(win32gui.GetForegroundWindow())[0], tid, True)
    ctrl = win32gui.GetFocus()
    buf_length = win32gui.SendMessage(ctrl, win32gui.WM_GETTEXTLENGTH, 0, 0) + 1
    buffer = win32gui.PyMakeBuffer(buf_length)
    win32gui.SendMessage(ctrl, win32gui.WM_GETTEXT, buf_length, buffer)
    win32gui.AttachThreadInput(win32gui.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[0], tid, False)
    return buffer[:]

if __name__ == "__main__":
    last_selected_text = ""
    while True:
        selected_text = get_selected_text()
        if selected_text != last_selected_text:
            print("选中的文本:", selected_text)
            last_selected_text = selected_text
        time.sleep(0.1)