import io
import json
import os
import subprocess
import sys
import threading
import urllib.request
from tkinter import filedialog, messagebox
 
import customtkinter as ctk
import yt_dlp
from PIL import Image
 
# ---------- tema ----------
BG = "#0f0f0f"
PANEL = "#181818"
CARD = "#202020"
CARD_HOVER = "#2a2a2a"
RED = "#ff0000"
RED_DARK = "#cc0000"
MUTED = "#8a8a8a"
GREEN = "#22c55e"
 
ctk.set_appearance_mode("dark")
QUALITIES = {
    "mp3": [
        ("Extreme", "320kbps • High Fidelity", "320"),
        ("Standard", "192kbps • Good Quality", "192"),
        ("Lite", "128kbps • Small Size", "128"),
        ("Low", "64kbps • Terendah", "64"),
    ],
    "mp4": [
        ("Highest", "Terbaik yang tersedia (hingga 4K)", "best"),
        ("High", "1080p • Full HD", "1080"),
        ("Standard", "720p • HD", "720"),
        ("Lowest", "Ukuran terkecil (144p-360p)", "worst"),
    ],
}