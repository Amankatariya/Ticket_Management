from enum import Enum

class StatusChoice(Enum):
    CREATED = 'CREATED'
    TO_DO = 'TO_DO'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'

STATUS_CHOICES = [
    (StatusChoice.CREATED.value, 'Created'),
    (StatusChoice.TO_DO.value, 'To Do'),
    (StatusChoice.IN_PROGRESS.value, 'In Progress'),
    (StatusChoice.DONE.value, 'Done'),
    (StatusChoice.CANCELLED.value, 'Cancelled')
]
