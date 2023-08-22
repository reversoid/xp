from aiogram import Router
from modules.experiment.handlers.run_experiment import router as _start_router
from modules.experiment.handlers.confirm_start_experiment import router as _confirm_start_router
from modules.experiment.handlers.cancel_experiment import router as _cancel_router
from modules.experiment.handlers.finish_experiment import router as _finish_router
from modules.experiment.handlers.handle_experiment import router as _handle_router


experiment_router = Router()

experiment_router.include_routers(
    _start_router,
    _confirm_start_router,
    _cancel_router,
    _finish_router,
    _handle_router
)
