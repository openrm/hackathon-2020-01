import evaluate_rotation_correction as rotation_correction
import evaluate_entity_extraction as entity_extraction

def resolve_task(task_id):
    if task_id == rotation_correction.INFO.id:
        return rotation_correction.INFO;
    elif task_id == entity_extraction.INFO.id:
        return entity_extraction.INFO;
