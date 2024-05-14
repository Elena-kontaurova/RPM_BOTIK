''' Файл '''
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.anketa import Anketa
from keyboards.anketa import kb_anketa_by_gender, kb_anketa_cancel, kb_anketa_cancel_and_back

router = Router()

@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    '''Метод - обработчик команды anketa. '''
    await state.set_state(Anketa.name)
    await msg.answer('Введите Ваше имя', reply_markup= kb_anketa_cancel)


@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод -  обработчик callback-запроса, с данными анкеты. 
Используется для отмены регистрации. Бот уведомляет пользователя 
сообщением 'Регистрация отменена'. '''
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    ''' Метод - обработки сообщения, в котором пользователь должен 
указать своё имя. '''
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    await msg.answer(
        'Введите Ваш возраст', reply_markup=kb_anketa_cancel_and_back)


@router.callback_query(F.data == 'back_anketa')
async def back_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод - обработчик callback-запросов. '''
    current_state = await state.get_state()
    if current_state == Anketa.gender:
        await state.set_state(Anketa.age)
        await callback_query.message.answer(
            'Введите Ваш возраст', reply_markup=kb_anketa_cancel_and_back)


    elif current_state == Anketa.age:
        await state.set_state(Anketa.name)
        await callback_query.message.answer(
            'Введите ваше имя', reply_markup= kb_anketa_cancel)


@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    ''' Метод используется для обработки ввода возраста пользоватлелем. '''
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы не верно ввели возраст!')
        await msg.answer(
            'Введите Ваш возраст', reply_markup=kb_anketa_cancel_and_back)
        return
    await state.set_state(Anketa.gender)
    await msg.answer(
        'Введите Ваш пол', 
        reply_markup= kb_anketa_by_gender)


@router.callback_query(F.data.startswith('gender_') and Anketa.gender)
async def set_gender_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    ''' Метод - обрабатывает нажание по кнопкам'''
    gender = {'gender_m': 'Мужской', 'gender_w': 'Женский'}[callback_query.data]
    await state.update_data(gender=gender)
    await callback_query.message.answer(str(await state.get_data()))
    await state.clear()


@router.message(Anketa.gender)
async def set_age_by_anketa_one_handler(msg: Message):
    ''' Метод - обрабатывает ввод пола'''
    await msg.answer('Нужно пол выбрать кнопкой')
