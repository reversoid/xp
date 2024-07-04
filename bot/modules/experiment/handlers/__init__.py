from aiogram import Router
from modules.experiment.handlers.start_experiment import router as _start_router
from modules.experiment.handlers.confirm_start_experiment import (
    router as _confirm_start_router,
)
from modules.experiment.handlers.complete_experiment import router as _handle_router
from modules.experiment.middlewares.experiment_scheduler_middleware import (
    ExperiementSchedulerMiddleware,
)
from shared.middlewares.subscription_middleware.subscription_middleware import (
    SubscriptionMiddleware,
)


experiment_router = Router()
experiment_router.message.middleware.register(ExperiementSchedulerMiddleware())
experiment_router.callback_query.middleware.register(ExperiementSchedulerMiddleware())

experiment_router.message.middleware.register(SubscriptionMiddleware())


experiment_router.include_routers(_start_router, _confirm_start_router, _handle_router)
