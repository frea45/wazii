# (c) @FarshidBand

import os


class Config(object):
	BOT_TOKEN = os.environ.get("5088657122:AAFlOm_612eSVMN-ML-akdXe2C-EhijqN9k")
	API_ID = int(os.environ.get("3335796", 12345))
	API_HASH = os.environ.get("138b992a0e672e8346d8439c3f42ea78")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("-1001482606933"))
	UPDATES_CHANNEL = os.environ.get("-1001482606933", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("ultrafast", "ultrafast")
	OWNER_ID = int(os.environ.get("763990585", 1445283714))
	CAPTION = "★ @FarshidBand ™"
	BOT_USERNAME = os.environ.get("fi2li123robot", "VideoWatermark_Bot")
	DATABASE_URL = os.environ.get("mongodb+srv://abirhasan2005:abirhasan@cluster0.lb2tp.mongodb.net/cluster0?retryWrites=true&w=majority")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
**👋 سلام دوست عزیز خوش آمدید ✨**

**🔘 من ربات کاربردی واترمارک فایل های ویدیویی هستم.** 

**✅ پشتیبانی از حداکثر حجم 2GB** 

**🎌 فعالیت ربات ← /status **
‌**⚙️⁩ تنظیمات واترمارک ← /settings** 

**👤 مدیر : [FāRSHíD-Band](https://t.me/FarshidBand)**
"""
	PROGRESS = """
• ✅{1} of 📁{2} •
📊 **درصد دانلود شده** : {0}%
🚀 **سرعت** : {3}/s
⁦⌚⁩ **مدت زمان اتمام پروژه** : {4}
"""
