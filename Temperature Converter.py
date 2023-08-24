import tkinter as tk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        self.temperature_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_label = tk.Label(self.root, text="Enter Temperature:")
        entry_label.pack()

        entry = tk.Entry(self.root, textvariable=self.temperature_var)
        entry.pack()

        convert_button = tk.Button(self.root, text="Convert", command=self.convert_temperature)
        convert_button.pack()

        result_label = tk.Label(self.root, textvariable=self.result_var)
        result_label.pack()

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_var.get())

            celsius = (temperature - 32) * 5/9
            fahrenheit = (temperature * 9/5) + 32

            self.result_var.set(f"{temperature:.2f} °F = {celsius:.2f} °C\n{temperature:.2f} °C = {fahrenheit:.2f} °F")
        except ValueError:
            self.result_var.set("Invalid input. Please enter a valid temperature.")

if __name__ == "__main__":
    root = tk.Tk()
    converter = TemperatureConverter(root)
    root.mainloop()
