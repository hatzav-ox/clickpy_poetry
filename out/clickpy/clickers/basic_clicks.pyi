from clickpy.clickers.click_protocol import SupportsClick as SupportsClick
from typing import Optional

class BasicRandomClickStrategy(SupportsClick):
    min_sleep_time: int
    max_sleep_time: int
    sleep_time: Optional[int]
    print_debug: Optional[bool]
    def click(self) -> None: ...

class FastClickStrategy(SupportsClick):
    sleep_time: int
    print_debug: Optional[bool]
    def click(self) -> None: ...
