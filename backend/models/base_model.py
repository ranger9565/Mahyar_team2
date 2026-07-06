from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    تمام مدل‌ها باید از این کلاس ارث‌بری کنند.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate(self, prompt: str, context: dict | None = None):
        """
        دریافت درخواست و تولید پاسخ
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """
        بررسی در دسترس بودن مدل
        """
        pass

