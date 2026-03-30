import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import webbrowser
from PIL import Image, ImageTk
from src.engine import PredictionEngine
from src import config
import cv2

# Set theme and color palette
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ImageAnalyzerGUI(ctk.CTk):
    """
    Main application window for the Vulgarism Image Analyzer.
    Provides a user-friendly interface for image uploading, visualization, and inference.
    """
    def __init__(self):
        """Initializes the GUI, prediction engine, and sets up the layout."""
        super().__init__()

        self.title(config.GUI_TITLE)
        self.geometry("950x750")
        self.minsize(850, 650)

        # Initialize engine
        self.engine = PredictionEngine()

        # Layout configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
            logo_image = Image.open(logo_path)
            self.logo_ctk_image = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(120, 120))
            self.logo_label = ctk.CTkLabel(self.sidebar_frame, image=self.logo_ctk_image, text="")
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        except Exception:
            self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="IMAGE\nANALYZER", 
                                           font=ctk.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Description
        self.desc_label = ctk.CTkLabel(self.sidebar_frame, text="AI tool for automatic\nmoderation of vulgar\nhand gestures in images.",
                                        font=ctk.CTkFont(size=12, slant="italic"), justify="center")
        self.desc_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        self.sidebar_button_upload = ctk.CTkButton(self.sidebar_frame, text="Upload Image", 
                                                   command=self._on_upload_click)
        self.sidebar_button_upload.grid(row=2, column=0, padx=20, pady=10)

        # Model Info Panel
        self.info_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.info_frame.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        
        self.info_title = ctk.CTkLabel(self.info_frame, text="Technical Details", 
                                       font=ctk.CTkFont(size=14, weight="bold"))
        self.info_title.pack(pady=(0, 5))
        
        self.info_stats = ctk.CTkLabel(self.info_frame, text=config.GUI_MODEL_STATS_TEXT,
                                       justify="left", font=ctk.CTkFont(size=11), cursor="hand2")
        self.info_stats.pack()
        self.info_stats.bind("<Button-1>", lambda e: webbrowser.open(config.GUI_GITHUB_URL))

        # Appearance Mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self._change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_optionemenu.set("Dark")

        # --- Main Content ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Header
        self.header_label = ctk.CTkLabel(self.main_frame, text=config.GUI_TITLE, 
                                         font=ctk.CTkFont(size=28, weight="bold"))
        self.header_label.grid(row=0, column=0, pady=(0, 20))

        # Preview Area
        self.preview_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.preview_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.preview_frame.grid_columnconfigure(0, weight=1)
        self.preview_frame.grid_rowconfigure(0, weight=1)

        self.image_label = ctk.CTkLabel(self.preview_frame, text="No image uploaded.\nPlease click 'Upload Image' to begin.",
                                        font=ctk.CTkFont(size=16))
        self.image_label.grid(row=0, column=0)

        # --- Result Panel ---
        self.result_frame = ctk.CTkFrame(self.main_frame, height=150, corner_radius=15)
        self.result_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        self.result_frame.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(self.result_frame, text="Ready for Analysis", 
                                         font=ctk.CTkFont(size=18, weight="bold"))
        self.status_label.grid(row=0, column=0, pady=(15, 5))

        # Confidence Meter
        self.confidence_label = ctk.CTkLabel(self.result_frame, text="Confidence: 0%")
        self.confidence_label.grid(row=1, column=0)

        self.confidence_bar = ctk.CTkProgressBar(self.result_frame, width=400)
        self.confidence_bar.grid(row=2, column=0, pady=(0, 20))
        self.confidence_bar.set(0)

        self.current_image_path = None

    def _on_upload_click(self):
        """Triggered when the user clicks 'Upload Image'. Opens a file dialog."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            self._process_image(file_path)

    def _process_image(self, file_path):
        """
        Loads the image, updates the preview, and runs the prediction engine.
        
        Args:
            file_path (str): Absolute path to the image file selected by the user.
        """
        self.current_image_path = file_path
        
        # Load and display image
        img = Image.open(file_path)
        
        # Calculate aspect ratio
        display_width = 500
        w, h = img.size
        display_height = int(h * (display_width / w))
        
        if display_height > 400:
            display_height = 400
            display_width = int(w * (display_height / h))

        ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(display_width, display_height))
        self.image_label.configure(image=ctk_image, text="")
        self.image_label.image = ctk_image

        # Run prediction
        result = self.engine.predict(image_path=file_path)
        self._update_ui_with_result(result)

    def _update_ui_with_result(self, result):
        """
        Updates the UI elements (status label, confidence meter) based on prediction results.
        
        Args:
            result (dict): The result dictionary returned by PredictionEngine.predict().
        """
        if not result["success"]:
            self.status_label.configure(text=f"Error: {result['message']}", text_color="red")
            self.confidence_bar.set(0)
            self.confidence_label.configure(text="Confidence: 0%")
            return

        label = result["label"]
        confidence = result["confidence"]
        
        if label == "middle_finger":
            status_text = "⚠️ VULGARISM DETECTED!"
            status_color = config.COLOR_VULGAR
        elif label == "no_hand":
            status_text = "✅ No Hands Detected (Safe)"
            status_color = config.COLOR_SAFE
        else:
            status_text = "✅ SAFE TO UPLOAD"
            status_color = config.COLOR_SAFE

        self.status_label.configure(text=status_text, text_color=status_color)
        
        if label == "no_hand":
            self.confidence_label.configure(text="Confidence: N/A")
            self.confidence_bar.set(0)
        else:
            self.confidence_label.configure(text=f"Confidence: {confidence*100:.1f}%")
            self.confidence_bar.set(confidence)
        
        # Change bar color based on result
        if label == "middle_finger":
            self.confidence_bar.configure(progress_color=config.COLOR_VULGAR)
        else:
            self.confidence_bar.configure(progress_color=config.COLOR_SAFE)

    def _change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = ImageAnalyzerGUI()
    app.mainloop()
