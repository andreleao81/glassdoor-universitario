from app.models.ProfessorEvaluationModel import ProfessorEvaluationModel
from app.models.ProfessorModel import ProfessorModel
from app.extensions import db

def get_evals_by_prof(prof_id) -> ProfessorEvaluationModel:
    """
    Get all evaluations by a professor
    """
    professor_evaluations = ProfessorEvaluationModel.query.with_entities(
        ProfessorEvaluationModel.id,
        ProfessorEvaluationModel.attendance,
        ProfessorEvaluationModel.punctuality,
        ProfessorEvaluationModel.availability_questions,
        ProfessorEvaluationModel.student_relationship,
        ProfessorEvaluationModel.professor_methodology,
        ProfessorEvaluationModel.professor_id
    ).filter(
        ProfessorEvaluationModel.professor_id == prof_id
    ).all()

    if not professor_evaluations:
        return None

    return professor_evaluations

