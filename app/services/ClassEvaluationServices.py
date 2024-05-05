from app.schemas.ClassEvaluationSchema import CollegeClassEvaluationSchema
from app.models.ClassEvaluationModel import CollegeClassEvaluationModel

def create_class_eval(data, class_id, user_id, professor_id):
    """
    Create a new class evaluation
    """
    college_class_evaluation = CollegeClassEvaluationSchema(
        class_code=class_id,
        user_id=user_id,
        professor_id=professor_id
    ).load(data)
    college_class_evaluation.save()
    return CollegeClassEvaluationSchema().dump(college_class_evaluation)


def get_class_eval(class_id, user_id, professor_id):

    college_class_evaluation = CollegeClassEvaluationModel.query.filter(
            CollegeClassEvaluationModel.user_id == user_id,
            CollegeClassEvaluationModel.class_code == class_id,
            CollegeClassEvaluationModel.professor_id == professor_id
        ).first()
    
    if not college_class_evaluation:
        return None
    
    return CollegeClassEvaluationSchema().dump(college_class_evaluation)


def get_class_evals(class_id):
    college_class_evaluations = CollegeClassEvaluationModel.query.filter(CollegeClassEvaluationModel.class_code == class_id).all()
    return CollegeClassEvaluationSchema(many=True).dump(college_class_evaluations)
    