COMPLETE_CURRENT_CONVERSATION = """
شما در حال انجام فرآیند دیگری هستید ✋🚫.
لطفا فرآیند فعلی را کامل یا کنسل کنید تا بتوانید فرآیند جدیدی را آغاز کنید.
"""

CONVERSATION_TIMEOUT_EXCEEDED = """
ما در حدود **{} دقیقه** منتظر پاسخ از سمت شما بودیم 🥱🕔.
چون در این مدت پاسخی از شما دریافت نکرده ایم فرآیند فعلی شما را کنسل کردیم.
لطفا مجدد درخواست انجام فرآیند را بدهید.
"""

BOT_ERROR_OCCURED = """
متاسفانه هنگام اجرای درخواست شما مشکلی رخ داده است.
ما این مشکل را برای بررسی به ادمین ها گزارش داده ایم.
لطفا دوباره تلاش کنید ♥.
"""

ADMIN_ERROR_REPORT = """
Error occured in our bot:

command:
**{}**

error text:
**{}**
"""

YOU_ARE_NOT_USER = """
برای استفاده از این قابلیت شما باید کاربر ربات باشید.
لطفا /start را ارسال کنید تا به ربات دسترسی پیدا کنید.
"""

YOU_ARE_NOT_ADMIN = "برای استفاده از این قابلیت شما باید ادمین ربات باشید."

YOU_ARE_NOT_PROGRAMMER = "برای استفاده از این قابلیت شما باید برنامه نویس ربات باشید."
