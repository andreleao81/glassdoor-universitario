from app.models.ProfessorEvaluationModel import ProfessorEvaluationModel




def get_professor_eval(prof_id, user_id, class_id):
    """
    Get a professor evaluation
    """
    professor_evaluation = ProfessorEvaluationModel.query.filter(
        ProfessorEvaluationModel.professor_id == prof_id,
        ProfessorEvaluationModel.user_id == user_id,
        ProfessorEvaluationModel.class_code == class_id
    ).first()

    if not professor_evaluation:
        return None

    return professor_evaluation