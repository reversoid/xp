from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.api_services.profile_api_service.responses import PaginatedObservations
from modules.admin.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from modules.admin.services import admin_service
from shared.utils.send.send_observations import send_observation, send_observations
from modules.admin.keyboards import (
    get_manage_observation_keyboard,
    get_show_more_waitlist_keyboard,
    AdminApproveObservationCallback,
    AdminDeleteObservationCallback,
    AdminShowMoreWaitlistCallback,
)

router: Router = Router()


@router.message(Command("waitlist"))
async def show_waitlist(message: Message, bot: Bot, state: FSMContext):
    observations: PaginatedObservations = await admin_service.get_waiting_observations(
        message.from_user.id,
    )

    if not observations.items:
        await message.answer(LEXICON["waitlist_empty"])
        return

    await message.answer(LEXICON["waitlist_show"])

    for o in observations.items:
        await send_observation(
            o,
            bot,
            tg_user_id=message.from_user.id,
            reply_markup=get_manage_observation_keyboard(o.id),
        )

    if observations.cursor:
        await message.answer(
            LEXICON["waitlist_can_show_more"],
            reply_markup=get_show_more_waitlist_keyboard(observations.cursor),
        )


@router.callback_query(AdminShowMoreWaitlistCallback.filter())
async def show_more_waitlist(query: CallbackQuery, bot: Bot):
    cursor = AdminShowMoreWaitlistCallback.unpack(query.data).cursor

    if not cursor:
        await query.message.edit_reply_markup(reply_markup=None)
        return

    observations: PaginatedObservations = await admin_service.get_waiting_observations(
        query.from_user.id, cursor
    )

    for o in observations.items:
        await send_observation(
            o,
            bot,
            tg_user_id=query.from_user.id,
            reply_markup=get_manage_observation_keyboard(o.id),
        )

    if observations.cursor:
        await query.message.answer(
            LEXICON["waitlist_can_show_more"],
            reply_markup=get_show_more_waitlist_keyboard(observations.cursor),
        )


@router.callback_query(AdminApproveObservationCallback.filter())
async def handle_approve(query: CallbackQuery, bot: Bot):
    observation_id = AdminApproveObservationCallback.unpack(query.data).observation_id

    await admin_service.approve_observation(query.from_user.id, observation_id)

    await query.message.edit_reply_markup(reply_markup=None)
    await query.answer(LEXICON["observation_approved"])


@router.callback_query(AdminDeleteObservationCallback.filter())
async def handle_approve(query: CallbackQuery, bot: Bot):
    observation_id = AdminDeleteObservationCallback.unpack(query.data).observation_id

    await admin_service.delete_observation(query.from_user.id, observation_id)

    await query.message.edit_reply_markup(reply_markup=None)
    await query.answer(LEXICON["observation_declined"])
