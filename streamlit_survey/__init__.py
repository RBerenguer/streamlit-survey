"""
Copyright 2023 Olivier Binette

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from streamlit_survey.streamlit_survey import StreamlitSurvey
from streamlit_survey.survey_component import (
    CheckBox,
    DateInput,
    MultiSelect,
    Radio,
    SelectBox,
    SelectSlider,
    Slider,
    SurveyComponent,
    TextArea,
    TextInput,
    TimeInput,
    Pills,
)

__all__ = [
    "StreamlitSurvey",
    "SurveyComponent",
    "TextInput",
    "TextArea",
    "MultiSelect",
    "SelectBox",
    "Radio",
    "SelectSlider" "Slider",
    "CheckBox",
    "DateInput",
    "TimeInput",
    "Pills",
]

__author__ = """Olivier Binette"""
__email__ = "olivier.binette@gmail.com"
__version__ = "1.0.2"
