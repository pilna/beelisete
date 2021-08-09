from __future__ import annotations
from abc import ABC, abstractmethod

import pygame

class Scene:

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        raise NotImplementedError()
