import playsound as play
import json, time, pyautogui
import random as ran
from PIL import Image


# get json
def readJson(filepath):
    with open(filepath, 'r') as fp:
        return json.load(fp)


def final_one():
    final_dic = readJson('final.json')
    play.playsound("opt_01.mp3")
    print("PRESS next arrow")
    from pynput.keyboard import Key, Listener

    answer_list_pinyin = []
    answer_list_sound = []

    def show_image():
        final_key = list(final_dic)
        random_final_key = ran.choice(final_key)
        print(random_final_key)
        if random_final_key != "img/wellDone.jpg":
            im = Image.open(random_final_key)  # random_final_key = random
            im.show()
        else:
            im = Image.open(random_final_key)
            im.show()
            print(final_key)
            main()
        answer_list_pinyin.append(random_final_key)
        answer_list_sound.append(final_dic[random_final_key][0])
        del final_dic[random_final_key]

    def on_key_press(key):
        if len(answer_list_pinyin) == 23:
            final_dic["img/wellDone.jpg"] = ["no audio"]

    def on_key_release(key):
        if key == Key.right:
            pyautogui.hotkey('ctrl', 'w')
            show_image()
        elif key == Key.space:
            if len(answer_list_sound) != 0:
                play.playsound(answer_list_sound[-1])
                print("listen!")
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.esc:
            print("BYE BYE!")
            pyautogui.hotkey("ctrl", "w")
            exit()

    with Listener(on_press=on_key_press, on_release=on_key_release) as Listener:
        Listener.join()


def final_two():
    final_dic = readJson('final.json')
    play.playsound("opt_02.mp3")
    print("PRESS next arrow")
    from pynput.keyboard import Key, Listener

    answer_list_pinyin = []
    answer_list_sound = []

    def show_image_and_play_sound():
        final_key = list(final_dic)
        random_final_key = ran.choice(final_key)
        if random_final_key != "img/wellDone.jpg":
            im = Image.open('img/what.jpg')
            im.show()
        else:
            im = Image.open(random_final_key)
            im.show()
            main()
        answer_list_pinyin.append(random_final_key)
        answer_list_sound.append(final_dic[random_final_key][0])
        play.playsound(answer_list_sound[-1])
        del final_dic[random_final_key]

    def on_key_press(key):
        if len(answer_list_sound) == 23:
            final_dic["img/wellDone.jpg"] = ["no audio"]

    def on_key_release(key):
        if key == Key.right:
            pyautogui.hotkey('ctrl', 'w')
            show_image_and_play_sound()
        elif key == Key.space:
            if len(answer_list_sound) != 0:
                play.playsound(answer_list_sound[-1])
                print("listen!")
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.tab:
            if len(answer_list_pinyin) != 0:
                pyautogui.hotkey("ctrl", "w")
                im = Image.open(answer_list_pinyin[-1])
                im.show()
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.esc:
            print("BYE BYE!")
            pyautogui.hotkey("ctrl", "w")
            exit()

    with Listener(on_press=on_key_press, on_release=on_key_release) as Listener:
        Listener.join()


def initial_one():
    initial_dic = readJson('initial.json')
    play.playsound("opt_01.mp3")
    print("PRESS next arrow")
    from pynput.keyboard import Key, Listener

    answer_list_pinyin = []
    answer_list_sound = []

    def show_image():
        initial_key = list(initial_dic)
        random_initial_key = ran.choice(initial_key)
        print(random_initial_key)
        if random_initial_key != "img/wellDone.jpg":
            im = Image.open(random_initial_key)  # random_initial_key = random
            im.show()
        else:
            im = Image.open(random_initial_key)
            im.show()
            print(initial_key)
            main()
        answer_list_pinyin.append(random_initial_key)
        answer_list_sound.append(initial_dic[random_initial_key][0])
        del initial_dic[random_initial_key]

    def on_key_press(key):
        if len(answer_list_pinyin) == 21:
            initial_dic["img/wellDone.jpg"] = ["no audio"]

    def on_key_release(key):
        if key == Key.right:
            pyautogui.hotkey('ctrl', 'w')
            show_image()
        elif key == Key.space:
            if len(answer_list_sound) != 0:
                play.playsound(answer_list_sound[-1])
                print("listen!")
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.esc:
            print("BYE BYE!")
            pyautogui.hotkey("ctrl", "w")
            exit()

    with Listener(on_press=on_key_press, on_release=on_key_release) as Listener:
        Listener.join()


def initial_two():
    initial_dic = readJson('initial.json')
    play.playsound("opt_02.mp3")
    print("PRESS next arrow")
    from pynput.keyboard import Key, Listener

    answer_list_pinyin = []
    answer_list_sound = []

    def show_image_and_play_sound():
        initial_key = list(initial_dic)
        random_initial_key = ran.choice(initial_key)
        if random_initial_key != "img/wellDone.jpg":
            im = Image.open('img/what.jpg')
            im.show()
        else:
            im = Image.open(random_initial_key)
            im.show()
            main()
        answer_list_pinyin.append(random_initial_key)
        answer_list_sound.append(initial_dic[random_initial_key][0])
        play.playsound(answer_list_sound[-1])
        del initial_dic[random_initial_key]

    def on_key_press(key):
        if len(answer_list_sound) == 21:
            initial_dic["img/wellDone.jpg"] = ["no audio"]

    def on_key_release(key):
        if key == Key.right:
            pyautogui.hotkey('ctrl', 'w')
            show_image_and_play_sound()
        elif key == Key.space:
            if len(answer_list_sound) != 0:
                play.playsound(answer_list_sound[-1])
                print("listen!")
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.tab:
            if len(answer_list_pinyin) != 0:
                pyautogui.hotkey("ctrl", "w")
                im = Image.open(answer_list_pinyin[-1])
                im.show()
            else:
                print("Try PRESS next arrow instead!")
        elif key == Key.esc:
            print("BYE BYE!")
            pyautogui.hotkey("ctrl", "w")
            exit()

    with Listener(on_press=on_key_press, on_release=on_key_release) as Listener:
        Listener.join()


def main_final():
    play.playsound("final_opt.mp3")
    print("Option 01: One alphabet will be displayed. Try to guess how it's pronounced.\n"
          "Option 02: One pronunciation will be played. Listen and try to guess the correct alphabet.")
    user_input = input('\nChoose your opt HERE --> [1 / 2] :  ')
    if user_input == '01' or user_input == '1':
        final_one()
    elif user_input == '02' or user_input == '2':
        final_two()


def main_initial():
    play.playsound("initial_opt.mp3")
    print("Option 01: One alphabet will be displayed. Try to guess how it's pronounced.\n"
          "Option 02: One pronunciation will be played. Listen and try to guess the correct alphabet.")
    user_input = input('\nChoose your opt HERE --> [1 / 2] : ')
    if user_input == '01' or user_input == '1':
        initial_one()
    elif user_input == '02' or user_input == '2':
        initial_two()


initial_state = []


def main():
    if len(initial_state) == 0:
        initial_state.append(0)
        print(".....STARTING PROGRAM.....")
        play.playsound("intro.mp3")
        opt = input("Final or Initial?\n Enter your choice here: ")
        if opt.lower() == "final" or opt.lower() == 'f':
            main_final()
        elif opt.lower() == "initial" or opt.lower() == 'i':
            main_initial()
    else:
        play.playsound("try_again.mp3")
        pyautogui.hotkey("ctrl", "w")  #close welldone image
        tryAgain = input("Try again? [Y/N] : ")
        if tryAgain.lower() == 'y' or tryAgain.lower() == "yes":
            print(".....STARTING PROGRAM.....")
            opt = input("Final or Initial?\n Enter your choice here: ")
            if opt.lower() == "final" or opt.lower() == 'f':
                main_final()
            elif opt.lower() == "initial" or opt.lower() == 'i':
                main_initial()
        elif tryAgain.lower() == 'n' or tryAgain.lower() == "no":
            print("BYE BYE!")
            exit()


main()
exit()
