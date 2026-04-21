import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("800x400")
        self.root.configure(bg="#1a1a1a")
        
        # Define time zones
        self.timezones = {
            "UTC": "UTC",
            "EST": "America/New_York",
            "CST": "America/Chicago",
            "MST": "America/Denver",
            "PST": "America/Los_Angeles",
            "GMT": "Europe/London",
            "CET": "Europe/Paris",
            "IST": "Asia/Kolkata",
            "JST": "Asia/Tokyo",
            "AEST": "Australia/Sydney"
        }
        
        self.clock_labels = {}
        self.create_clocks()
        self.update_time()
    
    def create_clocks(self):
        """Create clock displays for each timezone"""
        title_font = font.Font(family="Helvetica", size=14, weight="bold")
        time_font = font.Font(family="Courier", size=24, weight="bold")
        
        # Create main title
        title = tk.Label(self.root, text="World Time Zones", font=font.Font(family="Helvetica", size=20, weight="bold"), bg="#1a1a1a", fg="#00ff00")
        title.pack(pady=10)
        
        # Create frame for clocks
        frame = tk.Frame(self.root, bg="#1a1a1a")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create clock for each timezone (in 2 columns)
        row = 0
        col = 0
        for tz_name, tz_path in self.timezones.items():
            clock_frame = tk.Frame(frame, bg="#2a2a2a", relief=tk.SUNKEN, bd=2)
            clock_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            # Timezone name
            tz_label = tk.Label(clock_frame, text=tz_name, font=title_font, bg="#2a2a2a", fg="#00ff00")
            tz_label.pack(pady=5)
            
            # Time display
            time_label = tk.Label(clock_frame, text="00:00:00", font=time_font, bg="#2a2a2a", fg="#ffff00")
            time_label.pack(pady=10)
            
            self.clock_labels[tz_path] = time_label
            
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(row + 1):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            frame.grid_columnconfigure(i, weight=1)
    
    def update_time(self):
        """Update all clock displays"""
        for tz_path, label in self.clock_labels.items():
            tz = pytz.timezone(tz_path)
            current_time = datetime.now(tz).strftime("%H:%M:%S")
            label.config(text=current_time)
        
        # Schedule next update (every 1000ms)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()