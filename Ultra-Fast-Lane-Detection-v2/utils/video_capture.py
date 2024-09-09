import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os
import cv2

class VideoFramesDataset(Dataset):
    def __init__(self, frames_dir, transform=None):
        self.frames_dir = frames_dir
        self.transform = transform
        self.frames = sorted(os.listdir(frames_dir))  # Получаем список всех кадров

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, idx):
        img_name = os.path.join(self.frames_dir, self.frames[idx])
        image = Image.open(img_name)

        if self.transform:
            image = self.transform(image)

        return image
