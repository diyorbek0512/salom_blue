try:
    # Some environments (or newer/altered marshmallow builds) may not expose
    # __version_info__ which older libraries expect. Add a compatibility shim
    # early during startup so imports that check that attribute don't fail.
    import marshmallow as _marshmallow
    if not hasattr(_marshmallow, "__version_info__"):
        ver = getattr(_marshmallow, "__version__", None)
        if ver:
            try:
                _marshmallow.__version_info__ = tuple(int(x) for x in ver.split('.') if x.isdigit())
            except Exception:
                # fall back to a harmless empty tuple
                _marshmallow.__version_info__ = ()
except Exception:
    # If marshmallow isn't installed yet or something goes wrong, continue
    # and let the normal dependency errors surface later.
    pass

from aiogram import executor, types

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True, allowed_updates=types.AllowedUpdates.all())

