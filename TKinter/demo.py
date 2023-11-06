'''Hunter Knott, CS 3270, Utah Valley University'''
import tkinter as tk
from playsound import playsound

def main():
    def quit_program():
        print("Quitting program")
        quit()

    def give_dollar():
        print("Hooray! You get $1")

    def play_audio(file):
        playsound(file)

    window = tk.Tk()
    window.geometry("900x500")

    prompt_label = tk.Label(window, text="Give some names to these animals", font=("Helvetica", 16))
    prompt_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    quit_button = tk.Button(window, text="QUIT", command=quit_program)
    quit_button.grid(row=4, column=1, pady=30)

    dollar_button = tk.Button(window, text="SURPRISE", command=give_dollar)
    dollar_button.grid(row=2, column=0)

    cow_field = tk.Text(window, height=1, width=30)
    cow_field.grid(row=1, column=0, padx=10, pady=10)

    pig_field = tk.Text(window, height=1, width=30)
    pig_field.grid(row=1, column=1, padx=10, pady=10)

    chicken_field = tk.Text(window, height=1, width=30)
    chicken_field.grid(row=1, column=2, padx=10, pady=10)

    cow_frame = tk.Frame(window)
    cow_frame.grid(row=2, column=0, sticky='w')
    image = tk.PhotoImage(file="MinecraftCow.png")
    cow_image = image.subsample(2, 2)
    image_label = tk.Label(cow_frame, image=cow_image)
    image_label.grid(row=2, column=0, padx=10, pady=10)

    pig_frame = tk.Frame(window)
    pig_frame.grid(row=2, column=1, sticky='w')
    image = tk.PhotoImage(file="MinecraftPig.png")
    pig_image = image.subsample(2, 2)
    image_label = tk.Label(pig_frame, image=pig_image)
    image_label.grid(row=2, column=0, padx=10, pady=10)

    chicken_frame = tk.Frame(window)
    chicken_frame.grid(row=2, column=2, sticky='w')
    image = tk.PhotoImage(file="MinecraftChicken.png")
    chicken_image = image.subsample(2, 2)
    image_label = tk.Label(chicken_frame, image=chicken_image)
    image_label.grid(row=2, column=0, padx=10, pady=10)

    audio_files = ["CowNoise.mp3", "PigNoise.mp3", "ChickenNoise.mp3"]
    for i, audio_file in enumerate(audio_files):
        file_name = audio_file.split('.')[0]
        file_name = file_name.replace('N', ' N')
        audio_button = tk.Button(window, text=f"{file_name}", command=lambda file=audio_file: play_audio(file))
        audio_button.grid(row=3, column=i)

    window.mainloop()

if __name__ == "__main__":
    main()