from tethys_sdk.base import TethysAppBase


class Hydrolang(TethysAppBase):
    """
    Tethys app class for HydroLang.
    """

    name = 'HydroLang'
    description = 'HydroLang example in a Tethys App'
    package = 'hydrolang'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/sticker_uihilab2_white.png'
    root_url = 'hydrolang'
    color = '#c0392b'
    tags = ''
    enable_feedback = False
    feedback_emails = []